import { BodyPoseDef } from "./bodyPoses";

export interface Point2D {
  x: number;
  y: number;
}

export type Chain3 = [Point2D, Point2D, Point2D];

export interface SkeletalPose {
  head: { cx: number; cy: number; tilt: number };
  torso: Chain3; // [neck, spineMid, pelvis]
  leftArm: Chain3; // [shoulder, elbow, hand]
  rightArm: Chain3; // [shoulder, elbow, hand]
  leftLeg: Chain3; // [hip, knee, foot]
  rightLeg: Chain3; // [hip, knee, foot]
  hands: {
    left: { x: number; y: number; angle: number };
    right: { x: number; y: number; angle: number };
  };
  overhead: Point2D;
}

/**
 * Curva suave cubic-bezier in-out con ligero overshoot orgánico opcional.
 */
export function easeInOutCubic(t: number): number {
  const c = Math.max(0, Math.min(1, t));
  return c < 0.5 ? 4 * c * c * c : 1 - Math.pow(-2 * c + 2, 3) / 2;
}

function lerp(a: number, b: number, t: number): number {
  return a + (b - a) * t;
}

function lerpPoint(a: Point2D, b: Point2D, t: number): Point2D {
  return {
    x: lerp(a.x, b.x, t),
    y: lerp(a.y, b.y, t),
  };
}

function lerpChain(a: Chain3, b: Chain3, t: number): Chain3 {
  return [
    lerpPoint(a[0], b[0], t),
    lerpPoint(a[1], b[1], t),
    lerpPoint(a[2], b[2], t),
  ];
}

/**
 * Extrae una cadena de 3 articulaciones [raíz, articulación media, extremo]
 * a partir de cualquier path SVG de BodyPoseDef ("M x0 y0 L x1 y1 L x2 y2" o "M x0 y0 L x2 y2").
 */
export function parsePathToChain3(
  pathStr: string,
  defaultBendOffset = 0
): Chain3 {
  const matches = Array.from(
    pathStr.matchAll(/(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)/g)
  );
  const pts: Point2D[] = matches.map((m) => ({
    x: parseFloat(m[1]),
    y: parseFloat(m[2]),
  }));

  if (pts.length === 0) {
    return [
      { x: 200, y: 210 },
      { x: 200, y: 270 },
      { x: 200, y: 330 },
    ];
  }
  if (pts.length === 1) {
    return [pts[0], pts[0], pts[0]];
  }
  if (pts.length === 2) {
    const [p0, p2] = pts;
    const dx = p2.x - p0.x;
    const dy = p2.y - p0.y;
    const len = Math.hypot(dx, dy) || 1;
    const nx = -dy / len;
    const ny = dx / len;
    const mid: Point2D = {
      x: (p0.x + p2.x) * 0.5 + nx * defaultBendOffset,
      y: (p0.y + p2.y) * 0.5 + ny * defaultBendOffset,
    };
    return [p0, mid, p2];
  }
  return [pts[0], pts[1], pts[pts.length - 1]];
}

/**
 * Convierte cualquier BodyPoseDef estático del catálogo en un SkeletalPose articulado.
 */
export function extractSkeletalPose(pose: BodyPoseDef): SkeletalPose {
  const torso = parsePathToChain3(pose.torso, 0);
  const legSubpaths = pose.legs
    .split(/(?=M\s)/i)
    .map((s) => s.trim())
    .filter(Boolean);

  const leftLeg = parsePathToChain3(
    legSubpaths[0] || "M 200 330 L 150 460",
    -4
  );
  const rightLeg = parsePathToChain3(
    legSubpaths[1] || legSubpaths[0] || "M 200 330 L 250 460",
    4
  );

  const leftArm = parsePathToChain3(pose.leftArm, 6);
  const rightArm = parsePathToChain3(pose.rightArm, -6);

  // Separación anatómica de hombros: asegura que los brazos nazcan de los hombros y no del cuello
  const shoulderWidth = 28;
  if (Math.abs(leftArm[0].x - torso[0].x) < 14) {
    leftArm[0].x = torso[0].x - shoulderWidth;
    leftArm[0].y = torso[0].y + 10;
  }
  if (Math.abs(rightArm[0].x - torso[0].x) < 14) {
    rightArm[0].x = torso[0].x + shoulderWidth;
    rightArm[0].y = torso[0].y + 10;
  }

  return {
    head: {
      cx: pose.head.cx,
      cy: pose.head.cy,
      tilt: pose.head.tilt ?? 0,
    },
    torso,
    leftArm,
    rightArm,
    leftLeg,
    rightLeg,
    hands: {
      left: {
        x: pose.hands.left.x,
        y: pose.hands.left.y,
        angle: pose.hands.left.angle ?? 0,
      },
      right: {
        x: pose.hands.right.x,
        y: pose.hands.right.y,
        angle: pose.hands.right.angle ?? 0,
      },
    },
    overhead: {
      x: pose.overhead.x,
      y: pose.overhead.y,
    },
  };
}

/**
 * Interpola continuamente todas las articulaciones entre dos SkeletalPose.
 */
export function interpolateSkeletalPose(
  fromPose: SkeletalPose,
  toPose: SkeletalPose,
  rawProgress: number
): SkeletalPose {
  const t = easeInOutCubic(rawProgress);
  return {
    head: {
      cx: lerp(fromPose.head.cx, toPose.head.cx, t),
      cy: lerp(fromPose.head.cy, toPose.head.cy, t),
      tilt: lerp(fromPose.head.tilt, toPose.head.tilt, t),
    },
    torso: lerpChain(fromPose.torso, toPose.torso, t),
    leftArm: lerpChain(fromPose.leftArm, toPose.leftArm, t),
    rightArm: lerpChain(fromPose.rightArm, toPose.rightArm, t),
    leftLeg: lerpChain(fromPose.leftLeg, toPose.leftLeg, t),
    rightLeg: lerpChain(fromPose.rightLeg, toPose.rightLeg, t),
    hands: {
      left: {
        x: lerp(fromPose.hands.left.x, toPose.hands.left.x, t),
        y: lerp(fromPose.hands.left.y, toPose.hands.left.y, t),
        angle: lerp(fromPose.hands.left.angle, toPose.hands.left.angle, t),
      },
      right: {
        x: lerp(fromPose.hands.right.x, toPose.hands.right.x, t),
        y: lerp(fromPose.hands.right.y, toPose.hands.right.y, t),
        angle: lerp(fromPose.hands.right.angle, toPose.hands.right.angle, t),
      },
    },
    overhead: lerpPoint(fromPose.overhead, toPose.overhead, t),
  };
}

/**
 * Solver analítico de Cinemática Inversa de 2 huesos (Ley de Cosenos).
 * Dado el hombro/cadera (root) y el objetivo de mano/pie (target),
 * calcula la posición exacta del codo/rodilla respetando las longitudes óseas l1 y l2.
 */
export function solveTwoBoneIK(
  root: Point2D,
  target: Point2D,
  l1: number,
  l2: number,
  bendDirection: 1 | -1 = 1
): Chain3 {
  const dx = target.x - root.x;
  const dy = target.y - root.y;
  const rawDist = Math.hypot(dx, dy);
  const maxReach = Math.max(4, l1 + l2 - 0.5);
  const minReach = Math.max(2, Math.abs(l1 - l2) + 0.5);
  const d = Math.max(minReach, Math.min(maxReach, rawDist));

  const baseAngle = Math.atan2(dy, dx);
  const cosAngle1 = Math.max(
    -1,
    Math.min(1, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d))
  );
  const angle1 = Math.acos(cosAngle1);
  const jointAngle = baseAngle + bendDirection * angle1;

  const mid: Point2D = {
    x: root.x + Math.cos(jointAngle) * l1,
    y: root.y + Math.sin(jointAngle) * l1,
  };

  const clampedEnd: Point2D =
    rawDist > maxReach && rawDist > 0
      ? {
          x: root.x + (dx / rawDist) * maxReach,
          y: root.y + (dy / rawDist) * maxReach,
        }
      : target;

  return [root, mid, clampedEnd];
}

function chainLengths(chain: Chain3, minL1 = 44, minL2 = 44): [number, number] {
  const l1 = Math.max(
    minL1,
    Math.hypot(chain[1].x - chain[0].x, chain[1].y - chain[0].y)
  );
  const l2 = Math.max(
    minL2,
    Math.hypot(chain[2].x - chain[1].x, chain[2].y - chain[1].y)
  );
  return [l1, l2];
}

/**
 * Aplica cinemática inversa (IK) y ciclos procedurales continuos de 2 huesos
 * (caminar, correr, manipular, esfuerzo, agachar_recoger, respiración) sobre el esqueleto.
 */
export function applyProceduralSkeletalMotion(
  base: SkeletalPose,
  frame: number,
  proceduralMode = "estatico",
  isSpeaking = false
): {
  pose: SkeletalPose;
  lookOffset: Point2D;
} {
  // Clon profundo ligero
  const p: SkeletalPose = {
    head: { ...base.head },
    torso: [{ ...base.torso[0] }, { ...base.torso[1] }, { ...base.torso[2] }],
    leftArm: [
      { ...base.leftArm[0] },
      { ...base.leftArm[1] },
      { ...base.leftArm[2] },
    ],
    rightArm: [
      { ...base.rightArm[0] },
      { ...base.rightArm[1] },
      { ...base.rightArm[2] },
    ],
    leftLeg: [
      { ...base.leftLeg[0] },
      { ...base.leftLeg[1] },
      { ...base.leftLeg[2] },
    ],
    rightLeg: [
      { ...base.rightLeg[0] },
      { ...base.rightLeg[1] },
      { ...base.rightLeg[2] },
    ],
    hands: {
      left: { ...base.hands.left },
      right: { ...base.hands.right },
    },
    overhead: { ...base.overhead },
  };

  // Mirada 2.5D base según hacia dónde apunta la mano derecha o inclinación de cabeza
  const handFocusDx = (p.rightArm[2].x - 200) * 0.08;
  const handFocusDy = (p.rightArm[2].y - 210) * 0.03;
  const lookOffset: Point2D = {
    x: Math.max(-13, Math.min(14, handFocusDx + Math.sin(frame / 18) * 1.8)),
    y: Math.max(
      -6,
      Math.min(7, handFocusDy + (p.head.tilt > 6 ? 3 : p.head.tilt < -6 ? -3 : 0))
    ),
  };

  const [lArm1, lArm2] = chainLengths(p.leftArm, 42, 42);
  const [rArm1, rArm2] = chainLengths(p.rightArm, 42, 42);
  const [lLeg1, lLeg2] = chainLengths(p.leftLeg, 64, 66);
  const [rLeg1, rLeg2] = chainLengths(p.rightLeg, 64, 66);

  if (proceduralMode === "caminar" || proceduralMode === "correr") {
    const isRun = proceduralMode === "correr";
    const speed = isRun ? 2.7 : 4.2;
    const strideRadiusX = isRun ? 64 : 46;
    const liftHeight = isRun ? 34 : 20;
    const phase = frame / speed;

    // Rebote pélvico de doble frecuencia por paso
    const pelvisBob = Math.abs(Math.sin(phase)) * (isRun ? 10 : 6);
    const forwardLean = isRun ? 14 : 6;

    p.head.cx += forwardLean;
    p.head.cy -= pelvisBob * 0.6;
    p.head.tilt += isRun ? 8 : 3;
    p.torso[0].x += forwardLean * 0.85;
    p.torso[0].y -= pelvisBob * 0.6;
    p.torso[1].x += forwardLean * 0.45;
    p.torso[1].y -= pelvisBob * 0.5;
    p.torso[2].y -= pelvisBob * 0.4;

    const hip = p.torso[2];

    // Pierna izquierda (fase 0) y derecha (fase PI) con IK de rodilla hacia delante (-1 en SVG donde +X es derecha y +Y es abajo)
    const lPhase = phase;
    const rPhase = phase + Math.PI;

    const lFootTarget: Point2D = {
      x: hip.x + Math.sin(lPhase) * strideRadiusX,
      y: 458 - Math.max(0, Math.cos(lPhase)) * liftHeight,
    };
    const rFootTarget: Point2D = {
      x: hip.x + Math.sin(rPhase) * strideRadiusX,
      y: 458 - Math.max(0, Math.cos(rPhase)) * liftHeight,
    };

    p.leftLeg = solveTwoBoneIK(hip, lFootTarget, lLeg1, lLeg2, -1);
    p.rightLeg = solveTwoBoneIK(hip, rFootTarget, rLeg1, rLeg2, -1);

    // Balanceo opuesto de brazos con flexión natural de codo
    const shoulder = { x: p.torso[0].x, y: p.torso[0].y + 26 };
    const armSwingX = isRun ? 52 : 36;
    const armSwingY = isRun ? 24 : 12;

    const lHandTarget: Point2D = {
      x: shoulder.x - Math.sin(lPhase) * armSwingX,
      y: shoulder.y + 72 - Math.sin(lPhase) * armSwingY,
    };
    const rHandTarget: Point2D = {
      x: shoulder.x - Math.sin(rPhase) * armSwingX + 10,
      y: shoulder.y + 68 - Math.sin(rPhase) * armSwingY,
    };

    p.leftArm = solveTwoBoneIK(shoulder, lHandTarget, lArm1, lArm2, 1);
    p.rightArm = solveTwoBoneIK(shoulder, rHandTarget, rArm1, rArm2, 1);
    p.hands.left.x = p.leftArm[2].x;
    p.hands.left.y = p.leftArm[2].y;
    p.hands.right.x = p.rightArm[2].x;
    p.hands.right.y = p.rightArm[2].y;
    lookOffset.x = isRun ? 12 : 9;
  } else if (proceduralMode === "manipular") {
    // Trabajo activo de manos con articulación real de codo mediante IK
    const cycle = frame / 6.5;
    const rTarget: Point2D = {
      x: p.rightArm[2].x + Math.sin(cycle) * 14,
      y: p.rightArm[2].y + Math.cos(cycle * 1.5) * 10,
    };
    const lTarget: Point2D = {
      x: p.leftArm[2].x + Math.cos(cycle) * 10,
      y: p.leftArm[2].y - Math.sin(cycle) * 8,
    };
    p.rightArm = solveTwoBoneIK(p.rightArm[0], rTarget, rArm1, rArm2, 1);
    p.leftArm = solveTwoBoneIK(p.leftArm[0], lTarget, lArm1, lArm2, 1);
    p.hands.right.x = p.rightArm[2].x;
    p.hands.right.y = p.rightArm[2].y;
    p.hands.left.x = p.leftArm[2].x;
    p.hands.left.y = p.leftArm[2].y;
    lookOffset.x = 10;
    lookOffset.y = 4;
  } else if (proceduralMode === "esfuerzo") {
    const strain = Math.sin(frame * 0.32);
    const pushDown = Math.abs(Math.sin(frame / 8)) * 12;
    p.head.cy += pushDown * 0.5;
    p.torso[0].y += pushDown * 0.5;
    p.torso[1].x += 6;

    const rTarget: Point2D = {
      x: p.rightArm[2].x + strain * 2.5,
      y: p.rightArm[2].y + pushDown,
    };
    const lTarget: Point2D = {
      x: p.leftArm[2].x - strain * 2.5,
      y: p.leftArm[2].y + pushDown,
    };
    p.rightArm = solveTwoBoneIK(p.rightArm[0], rTarget, rArm1, rArm2, 1);
    p.leftArm = solveTwoBoneIK(p.leftArm[0], lTarget, lArm1, lArm2, 1);
    p.hands.right.x = p.rightArm[2].x;
    p.hands.right.y = p.rightArm[2].y;
    p.hands.left.x = p.leftArm[2].x;
    p.hands.left.y = p.leftArm[2].y;
    lookOffset.x = 11;
    lookOffset.y = 5;
  } else if (proceduralMode === "agachar_recoger") {
    const dip = Math.sin(frame / 5) * 14;
    p.head.cy += 16 + dip * 0.5;
    p.torso[0].y += 16 + dip * 0.5;
    p.torso[2].y += 12;
    p.leftLeg = solveTwoBoneIK(
      p.torso[2],
      p.leftLeg[2],
      lLeg1,
      lLeg2,
      -1
    );
    p.rightLeg = solveTwoBoneIK(
      p.torso[2],
      p.rightLeg[2],
      rLeg1,
      rLeg2,
      -1
    );
    const rTarget: Point2D = {
      x: p.rightArm[2].x + 12,
      y: p.rightArm[2].y + 22 + dip,
    };
    p.rightArm = solveTwoBoneIK(p.rightArm[0], rTarget, rArm1, rArm2, 1);
    p.hands.right.x = p.rightArm[2].x;
    p.hands.right.y = p.rightArm[2].y;
    lookOffset.x = 9;
    lookOffset.y = 6;
  } else {
    // Micro-articulación orgánica de respiración y habla con IK suave
    const talkWave = isSpeaking ? Math.sin(frame / 3.8) * 9 : 0;
    const idleWave = Math.sin(frame / 9.5) * 4.5;
    const rTarget: Point2D = {
      x: p.rightArm[2].x + talkWave * 0.6,
      y: p.rightArm[2].y + idleWave - Math.abs(talkWave) * 0.5,
    };
    const lTarget: Point2D = {
      x: p.leftArm[2].x - talkWave * 0.4,
      y: p.leftArm[2].y - idleWave * 0.8,
    };
    p.rightArm = solveTwoBoneIK(p.rightArm[0], rTarget, rArm1, rArm2, 1);
    p.leftArm = solveTwoBoneIK(p.leftArm[0], lTarget, lArm1, lArm2, -1);
    p.hands.right.x = p.rightArm[2].x;
    p.hands.right.y = p.rightArm[2].y;
    p.hands.left.x = p.leftArm[2].x;
    p.hands.left.y = p.leftArm[2].y;
  }

  return { pose: p, lookOffset };
}

export function chainToSvgPath(chain: Chain3, smooth = false): string {
  const [p0, p1, p2] = chain;
  if (smooth) {
    return `M ${p0.x.toFixed(1)} ${p0.y.toFixed(1)} Q ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`;
  }
  return `M ${p0.x.toFixed(1)} ${p0.y.toFixed(1)} L ${p1.x.toFixed(1)} ${p1.y.toFixed(1)} L ${p2.x.toFixed(1)} ${p2.y.toFixed(1)}`;
}
