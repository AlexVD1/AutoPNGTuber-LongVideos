import React from "react";
import { TipoComposicionVisual } from "../types";

export interface NarrativeStageProps {
  escenario?: string;
  composicionVisual?: TipoComposicionVisual;
  frame: number;
}

export const ESCENARIOS_OSCUROS_16X9: ReadonlySet<string> = new Set([
  "espacio_profundo",
  "lunar",
  "superficie_marte",
  "habitacion_noche",
  "abismo_oceanico",
  "red_subterranea",
  "nucleo_tierra",
  "tormenta_electrica",
  "cueva_cristales",
  "laboratorio",
  "laboratorio_penumbra",
  "zona_transicion",
  "manto_terrestre",
  "tunel_relativista",
  "cabina_nave",
  "plataforma_tren",
  "salon_billar_victoriano",
  "taller_inventor_victoriano",
  "saloon_oeste",
  "espacio_molecular",
  "laboratorio_baekeland",
  "infraestructura_electrica",
  "galeria_diseno_retro",
  "basurero_estratigrafico",
  "sabana_africana_atardecer",
  "cantera_puente_piedra",
  "arsenal_venecia_1638",
  "estrecho_tacoma_1940",
  "metropoli_rascacielos",
  "metropoli_noche_resplandor",
  "observatorio_astronomico_cumbre",
  "playa_costa_nocturna",
  "maqueta_urbana_interruptores",
  "santuario_cielo_estrellado",
  "comedor_familiar",
  "salon_comedor",
  "calle_cafe_corner",
  "despacho_einstein_1915",
  "acantilado_tormenta_costera",
  "tunel_viento_industrial",
  "espacio_cfd_tecnico",
  "anatomia_macro_ala",
  "nanoscopia_sem_queratina",
  "laboratorio_histologia_herbst",
  "estudio_estroboscopico_captura",
  "camara_anecoica_acustica",
  "hangar_crepusculo",
  "disco_acrecion_cinematico",
  "horizonte_sucesos_distorsion",
  "vacio_singularidad_cuantica",
    "tejado_suburbano_noche",
  "aula_green_bank_1961",
  "panaderia_cosmica_nebulosa",
  "autopista_orbital_exoplanetas",
  "sistema_estelar_zona_habitable",
  "oceano_subglaciar_europa",
  "laboratorio_sopa_primordial",
  "selva_jurasica",
  "fondo_oceanico_filosofos",
  "casino_estelar_drake",
  "umbral_gran_filtro",
  "galeria_museo_evolucion",
  "sabana_metabolica_split",
  "bosque_gorila_campamento_fuego",
  "laboratorio_biomecanica_pelvis",
  "arrecife_coral_submarino",
  "taller_litico_corteza_motora",
  "cementerio_hominidos_niebla",
  "abismo_cuello_botella_fuego",
  "vacio",
]);

export const NarrativeStage16x9: React.FC<NarrativeStageProps> = ({
  escenario = "vacio",
  frame,
}) => {
  switch (escenario) {
    case "tejado_suburbano_noche":
      return <TejadoSuburbanoNocheStage frame={frame} />;
    case "aula_green_bank_1961":
      return <AulaGreenBankStage frame={frame} />;
    case "panaderia_cosmica_nebulosa":
      return <PanaderiaCosmicaNebulosaStage frame={frame} />;
    case "autopista_orbital_exoplanetas":
      return <AutopistaOrbitalExoplanetasStage frame={frame} />;
    case "sistema_estelar_zona_habitable":
      return <SistemaEstelarZonaHabitableStage frame={frame} />;
    case "oceano_subglaciar_europa":
      return <OceanoSubglaciarEuropaStage frame={frame} />;
    case "laboratorio_sopa_primordial":
      return <LaboratorioSopaPrimordialStage frame={frame} />;
    case "selva_jurasica":
      return <SelvaJurasicaStage frame={frame} />;
    case "fondo_oceanico_filosofos":
      return <FondoOceanicoFilosofosStage frame={frame} />;
    case "casino_estelar_drake":
      return <CasinoEstelarDrakeStage frame={frame} />;
    case "umbral_gran_filtro":
      return <UmbralGranFiltroStage frame={frame} />;
    case "galeria_museo_evolucion":
      return <GaleriaMuseoEvolucionStage frame={frame} />;
    case "estadio_podio_biomasa":
      return <EstadioPodioBiomasaStage frame={frame} />;
    case "sabana_metabolica_split":
      return <SabanaMetabolicaSplitStage frame={frame} />;
    case "bosque_gorila_campamento_fuego":
      return <BosqueGorilaCampamentoFuegoStage frame={frame} />;
    case "laboratorio_biomecanica_pelvis":
      return <LaboratorioBiomecanicaPelvisStage frame={frame} />;
    case "pradera_cebra_refugio_tribal":
      return <PraderaCebraRefugioTribalStage frame={frame} />;
    case "arrecife_coral_submarino":
      return <ArrecifeCoralSubmarinoStage frame={frame} />;
    case "oceano_vs_parque_aereo":
      return <OceanoVsParqueAereoStage frame={frame} />;
    case "taller_litico_corteza_motora":
      return <TallerLiticoCortezaMotoraStage frame={frame} />;
    case "valle_rift_pleistoceno":
      return <ValleRiftPleistocenoStage frame={frame} />;
    case "cementerio_hominidos_niebla":
      return <CementerioHominidosNieblaStage frame={frame} />;
    case "abismo_cuello_botella_fuego":
      return <AbismoCuelloBotellaFuegoStage frame={frame} />;
    case "amanecer_sabana_acacia":
      return <AmanecerSabanaAcaciaStage frame={frame} />;
    case "acantilado_tormenta_costera":
      return <AcantiladoTormentaCosteraStage frame={frame} />;
    case "tunel_viento_industrial":
      return <TunelVientoIndustrialStage frame={frame} />;
    case "espacio_cfd_tecnico":
      return <EspacioCfdTecnicoStage frame={frame} />;
    case "anatomia_macro_ala":
      return <AnatomiaMacroAlaStage frame={frame} />;
    case "nanoscopia_sem_queratina":
      return <NanoscopiaSemQueratinaStage frame={frame} />;
    case "laboratorio_histologia_herbst":
      return <LaboratorioHistologiaHerbstStage frame={frame} />;
    case "estudio_estroboscopico_captura":
      return <EstudioEstroboscopicoCapturaStage frame={frame} />;
    case "camara_anecoica_acustica":
      return <CamaraAnecoicaAcusticaStage frame={frame} />;
    case "hangar_crepusculo":
      return <HangarCrepusculoStage frame={frame} />;
    case "despacho_einstein_1915":
      return <DespachoEinsteinStage frame={frame} />;
    case "disco_acrecion_cinematico":
      return <DiscoAcrecionStage frame={frame} />;
    case "horizonte_sucesos_distorsion":
      return <HorizonteSucesosStage frame={frame} />;
    case "vacio_singularidad_cuantica":
      return <VacioSingularidadStage frame={frame} />;
    case "comedor_familiar":
    case "salon_comedor":
      return <ComedorFamiliarStage frame={frame} />;
    case "calle_cafe_corner":
      return <CalleCafeCornerStage frame={frame} />;
    case "metropoli_noche_resplandor":
      return <MetropoliNocheResplandorStage frame={frame} />;
    case "observatorio_astronomico_cumbre":
      return <ObservatorioAstronomicoCumbreStage frame={frame} />;
    case "playa_costa_nocturna":
      return <PlayaCostaNocturnaStage frame={frame} />;
    case "maqueta_urbana_interruptores":
      return <MaquetaUrbanaInterruptoresStage frame={frame} />;
    case "santuario_cielo_estrellado":
      return <SantuarioCieloEstrelladoStage frame={frame} />;
    case "cantera_puente_piedra":
      return <CanteraPuentePiedraStage frame={frame} />;
    case "arsenal_venecia_1638":
      return <ArsenalVeneciaStage frame={frame} />;
    case "estrecho_tacoma_1940":
      return <EstrechoTacomaStage frame={frame} />;
    case "metropoli_rascacielos":
      return <MetropoliRascacielosStage frame={frame} />;
    case "laboratorio":
    case "laboratorio_neuro":
      return <LaboratorioStage frame={frame} />;
    case "espacio_profundo":
    case "vuelo_relativista":
    case "orbita_sol_estrellas":
      return <EspacioStage frame={frame} />;
    case "cabina_nave":
      return <CabinaNaveStage frame={frame} />;
    case "tunel_relativista":
      return <TunelRelativistaStage frame={frame} />;
    case "plataforma_tren":
      return <PlataformaTrenStage frame={frame} />;
    case "salon_billar_victoriano":
      return <SalonBillarStage frame={frame} />;
    case "taller_inventor_victoriano":
      return <TallerInventorStage frame={frame} />;
    case "saloon_oeste":
      return <SaloonOesteStage frame={frame} />;
    case "espacio_molecular":
      return <EspacioMolecularStage frame={frame} />;
    case "laboratorio_baekeland":
      return <LaboratorioBaekelandStage frame={frame} />;
    case "infraestructura_electrica":
      return <InfraestructuraElectricaStage frame={frame} />;
    case "galeria_diseno_retro":
      return <GaleriaDisenoRetroStage frame={frame} />;
    case "basurero_estratigrafico":
      return <BasureroEstratigraficoStage frame={frame} />;
    case "sabana_africana_atardecer":
      return <SabanaAfricanaStage frame={frame} />;
    case "lunar":
    case "superficie_marte":
      return <SuperficieCosmicaStage frame={frame} marte={escenario === "superficie_marte"} />;
    case "habitacion_noche":
      return <HabitacionNocheStage frame={frame} />;
    case "abismo_oceanico":
      return <AbismoOceanicoStage frame={frame} />;
    case "red_subterranea":
      return <RedSubterraneaStage frame={frame} />;
    case "zona_transicion":
    case "manto_terrestre":
      return <ZonaTransicionStage frame={frame} />;
    case "fondo_escolar":
      return <FondoEscolarStage frame={frame} />;
    case "cielo_dia":
    case "atardecer_dorado":
      return <CieloStage frame={frame} atardecer={escenario === "atardecer_dorado"} />;
    case "vacio":
    default:
      return <VacioStage frame={frame} />;
  }
};

/** Fondo minimalista neo-brutal con cuadrícula matemática limpia */
const VacioStage: React.FC<{ frame: number }> = () => {
  return (
    <div
      className="absolute inset-0 pointer-events-none z-0"
      style={{
        backgroundColor: "#0B1120",
        backgroundImage: "radial-gradient(#334155 2px, transparent 2px)",
        backgroundSize: "40px 40px",
      }}
    >
      <div
        className="absolute inset-0"
        style={{
          background: "radial-gradient(circle at 50% 50%, transparent 60%, rgba(2, 6, 23, 0.7) 100%)",
        }}
      />
    </div>
  );
};

/** Laboratorio científico 16:9 con pantallas y aparatos */
const LaboratorioStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pulse = Math.sin(frame / 10) * 0.2 + 0.8;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="labWall" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E293B" />
            <stop offset="70%" stopColor="#0F172A" />
            <stop offset="100%" stopColor="#020617" />
          </linearGradient>
          <linearGradient id="labFloor" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#334155" />
            <stop offset="100%" stopColor="#0F172A" />
          </linearGradient>
        </defs>

        {/* Pared trasera */}
        <rect x="0" y="0" width="1920" height="780" fill="url(#labWall)" />

        {/* Paneles de pared tecnológicos */}
        {Array.from({ length: 8 }).map((_, i) => (
          <line
            key={i}
            x1={i * 240 + 120}
            y1="0"
            x2={i * 240 + 120}
            y2="780"
            stroke="#334155"
            strokeWidth="3"
            strokeDasharray="16 8"
          />
        ))}

        {/* Piso de laboratorio con perspectiva */}
        <polygon points="0,780 1920,780 1920,1080 0,1080" fill="url(#labFloor)" />
        <line x1="0" y1="780" x2="1920" y2="780" stroke="#000000" strokeWidth="6" />

        {/* Rejilla de perspectiva en piso */}
        {[-3, -2, -1, 0, 1, 2, 3].map((pos) => (
          <line
            key={pos}
            x1={960 + pos * 180}
            y1="780"
            x2={960 + pos * 360}
            y2="1080"
            stroke="#1E293B"
            strokeWidth="3"
          />
        ))}

        {/* Pantalla holográfica lateral izquierda */}
        <g transform="translate(140, 240)">
          <rect
            width="280"
            height="180"
            rx="12"
            fill="#0284C7"
            fillOpacity={0.15}
            stroke="#38BDF8"
            strokeWidth="4"
          />
          <text x="20" y="40" fill="#38BDF8" fontSize="16" fontWeight="bold">
            DATA SPECTROMETRY
          </text>
          <path
            d={`M 20 120 Q 80 ${90 + Math.sin(frame / 6) * 20} 140 120 T 260 120`}
            fill="none"
            stroke="#38BDF8"
            strokeWidth="3"
          />
          <circle cx="240" cy="40" r="6" fill="#38BDF8" opacity={pulse} />
        </g>

        {/* Estación de monitores derecha */}
        <g transform="translate(1500, 260)">
          <rect
            width="260"
            height="160"
            rx="12"
            fill="#0F766E"
            fillOpacity={0.15}
            stroke="#2DD4BF"
            strokeWidth="4"
          />
          <text x="20" y="38" fill="#2DD4BF" fontSize="16" fontWeight="bold">
            SIGNAL ANALYSIS
          </text>
          <line x1="20" y1="70" x2="240" y2="70" stroke="#134E4A" strokeWidth="2" />
          <line x1="20" y1="100" x2="240" y2="100" stroke="#134E4A" strokeWidth="2" />
          <line x1="20" y1="130" x2="240" y2="130" stroke="#134E4A" strokeWidth="2" />
          <rect
            x="25"
            y={80 + Math.sin(frame / 8) * 10}
            width="50"
            height="8"
            fill="#2DD4BF"
          />
        </g>
      </svg>
    </div>
  );
};

/** Espacio profundo 16:9 con nebulosas, estrellas y horizonte cósmico */
const EspacioStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#030712] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="nebulaA" cx="70%" cy="30%" r="50%">
            <stop offset="0%" stopColor="#4F46E5" stopOpacity="0.45" />
            <stop offset="60%" stopColor="#7C3AED" stopOpacity="0.15" />
            <stop offset="100%" stopColor="#030712" stopOpacity="0" />
          </radialGradient>
          <radialGradient id="nebulaB" cx="25%" cy="65%" r="45%">
            <stop offset="0%" stopColor="#06B6D4" stopOpacity="0.35" />
            <stop offset="60%" stopColor="#0284C7" stopOpacity="0.1" />
            <stop offset="100%" stopColor="#030712" stopOpacity="0" />
          </radialGradient>
        </defs>

        <rect width="1920" height="1080" fill="url(#nebulaA)" />
        <rect width="1920" height="1080" fill="url(#nebulaB)" />

        {/* Campo estelar multicapa con centelleo */}
        {Array.from({ length: 85 }).map((_, i) => {
          const x = (i * 127 + frame * 0.2) % 1920;
          const y = (i * 83) % 1080;
          const r = (i % 3) + 1.2;
          const opacity = Math.sin((frame + i * 14) / 10) * 0.4 + 0.6;
          const isColored = i % 7 === 0;
          return (
            <circle
              key={i}
              cx={x}
              cy={y}
              r={r}
              fill={isColored ? "#38BDF8" : "#FFFFFF"}
              opacity={opacity}
            />
          );
        })}

        {/* Planeta lejano en la esquina superior derecha */}
        <g transform="translate(1620, 220)">
          <circle cx="0" cy="0" r="70" fill="#1E1B4B" stroke="#6366F1" strokeWidth="3" />
          <ellipse
            cx="0"
            cy="0"
            rx="110"
            ry="24"
            fill="none"
            stroke="#818CF8"
            strokeWidth="4"
            transform="rotate(-22)"
          />
        </g>
      </svg>
    </div>
  );
};

/** Superficie lunar o marciana 16:9 con cráteres y horizonte */
const SuperficieCosmicaStage: React.FC<{ frame: number; marte?: boolean }> = ({
  marte = false,
}) => {
  const skyColor = marte ? "#1C0A00" : "#020617";
  const soilDark = marte ? "#7C2D12" : "#334155";
  const soilLight = marte ? "#C2410C" : "#64748B";

  return (
    <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden" style={{ backgroundColor: skyColor }}>
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Cielo con estrellas */}
        {Array.from({ length: 50 }).map((_, i) => (
          <circle
            key={i}
            cx={(i * 149) % 1920}
            cy={(i * 61) % 650}
            r={(i % 2) + 1.2}
            fill="#FFFFFF"
            opacity={0.7}
          />
        ))}

        {/* Cordillera lejana */}
        <path
          d="M 0 680 L 250 630 L 520 660 L 850 610 L 1200 650 L 1550 590 L 1920 640 L 1920 1080 L 0 1080 Z"
          fill={soilDark}
          stroke="#000000"
          strokeWidth="4"
        />

        {/* Colina en primer plano */}
        <path
          d="M 0 760 Q 480 710 960 750 T 1920 740 L 1920 1080 L 0 1080 Z"
          fill={soilLight}
          stroke="#000000"
          strokeWidth="5"
        />

        {/* Cráteres en suelo */}
        <ellipse cx="420" cy="880" rx="90" ry="24" fill={soilDark} stroke="#000000" strokeWidth="4" />
        <ellipse cx="1400" cy="920" rx="140" ry="32" fill={soilDark} stroke="#000000" strokeWidth="4" />
      </svg>
    </div>
  );
};

/** Habitación nocturna 16:9 con ventana, luna y piso */
const HabitacionNocheStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#090D16] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Pared interior */}
        <rect width="1920" height="800" fill="#0F172A" />

        {/* Ventana grande con vista a la noche */}
        <g transform="translate(1320, 160)">
          <rect width="420" height="480" rx="16" fill="#020617" stroke="#000000" strokeWidth="8" />
          {/* Luna */}
          <circle cx="320" cy="110" r="45" fill="#FEF08A" stroke="#000000" strokeWidth="4" />
          {/* Estrellas en ventana */}
          <circle cx="80" cy="90" r="3" fill="#FFFFFF" />
          <circle cx="160" cy="180" r="2" fill="#FFFFFF" />
          <circle cx="110" cy="300" r="3" fill="#FFFFFF" />
          {/* Marco de ventana */}
          <line x1="210" y1="0" x2="210" y2="480" stroke="#000000" strokeWidth="8" />
          <line x1="0" y1="240" x2="420" y2="240" stroke="#000000" strokeWidth="8" />
        </g>

        {/* Estantería de libros a la izquierda */}
        <g transform="translate(140, 220)">
          <rect width="320" height="420" fill="#1E293B" stroke="#000000" strokeWidth="6" />
          <line x1="0" y1="140" x2="320" y2="140" stroke="#000000" strokeWidth="6" />
          <line x1="0" y1="280" x2="320" y2="280" stroke="#000000" strokeWidth="6" />
          {/* Libros */}
          <rect x="25" y="60" width="28" height="80" fill="#EF4444" stroke="#000000" strokeWidth="3" />
          <rect x="58" y="45" width="34" height="95" fill="#3B82F6" stroke="#000000" strokeWidth="3" />
          <rect x="97" y="70" width="24" height="70" fill="#EAB308" stroke="#000000" strokeWidth="3" />
        </g>

        {/* Piso de madera */}
        <rect x="0" y="800" width="1920" height="280" fill="#78350F" stroke="#000000" strokeWidth="6" />
        {Array.from({ length: 6 }).map((_, i) => (
          <line
            key={i}
            x1="0"
            y1={800 + i * 45}
            x2="1920"
            y2={800 + i * 45}
            stroke="#451A03"
            strokeWidth="3"
          />
        ))}
      </svg>
    </div>
  );
};

/** Abismo oceánico 16:9 con gradiente abisal y medusas */
const AbismoOceanicoStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#020617] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="abyssGradient" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0C4A6E" />
            <stop offset="40%" stopColor="#075985" />
            <stop offset="80%" stopColor="#032B44" />
            <stop offset="100%" stopColor="#020617" />
          </linearGradient>
        </defs>

        <rect width="1920" height="1080" fill="url(#abyssGradient)" />

        {/* Rayos cenitales de luz */}
        <polygon points="400,0 600,0 850,1080 300,1080" fill="#38BDF8" fillOpacity={0.06} />
        <polygon points="1200,0 1400,0 1700,1080 1150,1080" fill="#38BDF8" fillOpacity={0.05} />

        {/* Burbujas flotantes */}
        {Array.from({ length: 30 }).map((_, i) => {
          const speed = 2 + (i % 3);
          const y = ((1200 - (frame * speed + i * 90)) % 1300) - 100;
          const x = (i * 123 + Math.sin((frame + i * 10) / 10) * 20) % 1920;
          const r = 5 + (i % 6) * 3;
          return (
            <circle
              key={i}
              cx={x}
              cy={y}
              r={r}
              fill="none"
              stroke="#38BDF8"
              strokeWidth="2"
              opacity={0.6}
            />
          );
        })}

        {/* Suelo marino */}
        <path
          d="M 0 920 Q 480 870 960 910 T 1920 890 L 1920 1080 L 0 1080 Z"
          fill="#0B132B"
          stroke="#000000"
          strokeWidth="6"
        />
      </svg>
    </div>
  );
};

/** Red subterránea (micelio y raíces) 16:9 */
const RedSubterraneaStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1C1917] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <rect width="1920" height="1080" fill="#1C1917" />
        {/* Raíces principales y ramificaciones */}
        {Array.from({ length: 12 }).map((_, i) => {
          const x1 = (i * 180) % 1920;
          const pulse = Math.sin((frame + i * 20) / 8) * 0.3 + 0.7;
          return (
            <path
              key={i}
              d={`M ${x1} 0 Q ${x1 + 60} 300 ${x1 - 40} 600 T ${x1 + 50} 1080`}
              fill="none"
              stroke="#A8A29E"
              strokeWidth="5"
              strokeDasharray="14 6"
              opacity={pulse}
            />
          );
        })}
      </svg>
    </div>
  );
};

/** Cielo abierto 16:9 día o atardecer */
const CieloStage: React.FC<{ frame: number; atardecer?: boolean }> = ({
  frame,
  atardecer = false,
}) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
            {atardecer ? (
              <>
                <stop offset="0%" stopColor="#4C1D95" />
                <stop offset="45%" stopColor="#BE185D" />
                <stop offset="75%" stopColor="#F97316" />
                <stop offset="100%" stopColor="#FEF08A" />
              </>
            ) : (
              <>
                <stop offset="0%" stopColor="#0284C7" />
                <stop offset="50%" stopColor="#38BDF8" />
                <stop offset="85%" stopColor="#BAE6FD" />
                <stop offset="100%" stopColor="#E0F2FE" />
              </>
            )}
          </linearGradient>
        </defs>
        <rect width="1920" height="1080" fill="url(#skyGrad)" />
        {/* Nubes flotantes */}
        {Array.from({ length: 5 }).map((_, i) => {
          const x = ((i * 450 + frame * 0.8) % 2400) - 300;
          const y = 140 + i * 80;
          return (
            <ellipse
              key={i}
              cx={x}
              cy={y}
              rx={160}
              ry={45}
              fill="#FFFFFF"
              fillOpacity={0.65}
            />
          );
        })}
      </svg>
    </div>
  );
};

/** Zona de Transición del Manto (410 - 660 km): Rocas ultramáficas, presión colosal y resplandor de cristales azules */
const ZonaTransicionStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pulse = Math.sin(frame / 14) * 0.25 + 0.75;
  const shimmer = Math.cos(frame / 20) * 0.2 + 0.8;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#050C14] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="mantleGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#132719" />
            <stop offset="35%" stopColor="#0B1C28" />
            <stop offset="70%" stopColor="#0A183A" />
            <stop offset="100%" stopColor="#020617" />
          </linearGradient>
          <radialGradient id="ringwooditeGlow" cx="50%" cy="60%" r="55%">
            <stop offset="0%" stopColor="#2563EB" stopOpacity="0.4" />
            <stop offset="45%" stopColor="#0284C7" stopOpacity="0.18" />
            <stop offset="100%" stopColor="#050C14" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Fondo con gradiente profundo */}
        <rect width="1920" height="1080" fill="url(#mantleGrad)" />
        <rect width="1920" height="1080" fill="url(#ringwooditeGlow)" opacity={pulse} />

        {/* Capas estratigráficas de compresión tectónica */}
        <path
          d="M 0 340 Q 480 320 960 350 T 1920 330 L 1920 490 L 0 490 Z"
          fill="#0F241E"
          opacity={0.5}
        />
        <path
          d="M 0 490 Q 520 470 1080 500 T 1920 480 L 1920 780 L 0 780 Z"
          fill="#091E36"
          opacity={0.65}
        />
        <path
          d="M 0 780 Q 450 760 980 790 T 1920 770 L 1920 1080 L 0 1080 Z"
          fill="#061224"
          opacity={0.85}
        />

        {/* Marcadores de cota de profundidad científica */}
        <g opacity={0.65}>
          <line x1="80" y1="340" x2="1840" y2="340" stroke="#10B981" strokeWidth="2" strokeDasharray="12 8" />
          <text x="100" y="325" fill="#34D399" fontSize="18" fontWeight="bold" letterSpacing="3">
            ▲ 410 KM — LÍMITE OLIVINO → WADSLEYITA
          </text>

          <line x1="80" y1="520" x2="1840" y2="520" stroke="#38BDF8" strokeWidth="2" strokeDasharray="16 10" />
          <text x="100" y="505" fill="#38BDF8" fontSize="20" fontWeight="bold" letterSpacing="3">
            ◆ 525 KM — ZONA DE RINGWOODITA HIDRATADA
          </text>

          <line x1="80" y1="780" x2="1840" y2="780" stroke="#6366F1" strokeWidth="2" strokeDasharray="12 8" />
          <text x="100" y="765" fill="#818CF8" fontSize="18" fontWeight="bold" letterSpacing="3">
            ▼ 660 KM — TRANSICIÓN A BRIDGMANITA (MANTO INFERIOR)
          </text>
        </g>

        {/* Red cristalina hexagonal flotante (simbolizando la estructura de silicato) */}
        {Array.from({ length: 18 }).map((_, i) => {
          const cx = (i * 155 + 70 + Math.sin(frame / 30 + i) * 15) % 1920;
          const cy = 380 + ((i * 85) % 360) + Math.cos((frame + i * 10) / 25) * 12;
          const r = 24 + (i % 4) * 8;
          return (
            <g key={i} transform={`translate(${cx}, ${cy}) rotate(${frame * 0.3 + i * 20})`} opacity={0.45 * shimmer}>
              <polygon
                points="0,-20 17,-10 17,10 0,20 -17,10 -17,-10"
                fill="none"
                stroke={i % 2 === 0 ? "#38BDF8" : "#34D399"}
                strokeWidth="2.5"
                transform={`scale(${r / 20})`}
              />
              <circle cx="0" cy="0" r="3" fill="#67E8F9" />
            </g>
          );
        })}

        {/* Partículas de iones hidroxilo (-OH) y presión mineral */}
        {Array.from({ length: 45 }).map((_, i) => {
          const x = (i * 97 + frame * 0.4) % 1920;
          const y = 300 + ((i * 61 + frame * 0.25) % 550);
          const size = (i % 3) + 2;
          const op = Math.sin((frame + i * 17) / 12) * 0.4 + 0.6;
          return (
            <circle
              key={i}
              cx={x}
              cy={y}
              r={size}
              fill={i % 3 === 0 ? "#67E8F9" : "#38BDF8"}
              opacity={op}
            />
          );
        })}
      </svg>
    </div>
  );
};

/** Fondo escolar didáctico con papel cuadriculado y estética de libro de texto */
const FondoEscolarStage: React.FC<{ frame: number }> = () => {
  return (
    <div
      className="absolute inset-0 pointer-events-none z-0"
      style={{
        backgroundColor: "#F8FAFC",
        backgroundImage:
          "linear-gradient(#E2E8F0 1px, transparent 1px), linear-gradient(90deg, #E2E8F0 1px, transparent 1px)",
        backgroundSize: "36px 36px",
      }}
    >
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Margen rojo de cuaderno a la izquierda */}
        <line x1="140" y1="0" x2="140" y2="1080" stroke="#FCA5A5" strokeWidth="3" />

        {/* Diagrama didáctico escolar tenue en esquina superior derecha */}
        <g transform="translate(1550, 180)" opacity="0.35">
          {/* Sol sonriente */}
          <circle cx="0" cy="0" r="45" fill="#FDE047" stroke="#000000" strokeWidth="4" />
          {/* Nube con lluvia */}
          <path
            d="M 120 40 Q 140 10 180 20 Q 220 10 240 40 Q 270 50 260 80 Q 250 110 210 110 L 130 110 Q 100 100 120 40 Z"
            fill="#BAE6FD"
            stroke="#000000"
            strokeWidth="4"
          />
          {/* Gotas */}
          <line x1="160" y1="130" x2="150" y2="155" stroke="#0284C7" strokeWidth="4" strokeDasharray="6 6" />
          <line x1="190" y1="130" x2="180" y2="155" stroke="#0284C7" strokeWidth="4" strokeDasharray="6 6" />
          <line x1="220" y1="130" x2="210" y2="155" stroke="#0284C7" strokeWidth="4" strokeDasharray="6 6" />
        </g>
      </svg>
    </div>
  );
};

/** Plataforma de Tren Clásica (Experimento Mental Galileo vs Luz) */
const PlataformaTrenStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="trainSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E293B" />
            <stop offset="60%" stopColor="#334155" />
            <stop offset="100%" stopColor="#475569" />
          </linearGradient>
        </defs>

        {/* Fondo cielo / estación */}
        <rect width="1920" height="750" fill="url(#trainSky)" />

        {/* Vigas de la estación en perspectiva */}
        {Array.from({ length: 9 }).map((_, i) => {
          const x = i * 240 + 60;
          return (
            <g key={i}>
              <line x1={x} y1="0" x2={x - 80} y2="750" stroke="#1E293B" strokeWidth="8" />
              <line x1={x - 80} y1="200" x2={x + 160} y2="200" stroke="#0F172A" strokeWidth="6" />
            </g>
          );
        })}

        {/* Plataforma de hormigón */}
        <rect x="0" y="750" width="1920" height="120" fill="#64748B" stroke="#000000" strokeWidth="6" />

        {/* Franja de seguridad amarilla y negra (hazard stripes) */}
        {Array.from({ length: 48 }).map((_, i) => (
          <polygon
            key={i}
            points={`${i * 42},750 ${i * 42 + 24},750 ${i * 42},780 ${i * 42 - 24},780`}
            fill="#F59E0B"
          />
        ))}
        <line x1="0" y1="780" x2="1920" y2="780" stroke="#000000" strokeWidth="4" />

        {/* Vías del tren en el tercio inferior */}
        <rect x="0" y="870" width="1920" height="210" fill="#1E293B" />
        {/* Durmientes de vía */}
        {Array.from({ length: 32 }).map((_, i) => {
          const x = (i * 65 + (frame * 4) % 65);
          return (
            <line
              key={i}
              x1={x}
              y1="900"
              x2={x}
              y2="1050"
              stroke="#475569"
              strokeWidth="16"
            />
          );
        })}
        {/* Rieles de acero brillantes */}
        <line x1="0" y1="930" x2="1920" y2="930" stroke="#94A3B8" strokeWidth="8" />
        <line x1="0" y1="934" x2="1920" y2="934" stroke="#F8FAFC" strokeWidth="3" />
        <line x1="0" y1="1020" x2="1920" y2="1020" stroke="#94A3B8" strokeWidth="8" />
        <line x1="0" y1="1024" x2="1920" y2="1024" stroke="#F8FAFC" strokeWidth="3" />
      </svg>
    </div>
  );
};

/** Cabina de Nave Espacial Relativista con parabrisas panorámico y HUD */
const CabinaNaveStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#020617] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="cockpitGlass" cx="50%" cy="40%" r="60%">
            <stop offset="0%" stopColor="#1E1B4B" stopOpacity="0.4" />
            <stop offset="70%" stopColor="#0F172A" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#020617" stopOpacity="1" />
          </radialGradient>
        </defs>

        {/* Espacio exterior visible por el ventanal */}
        <rect width="1920" height="850" fill="#030712" />

        {/* Estrellas cruzando velozmente */}
        {Array.from({ length: 65 }).map((_, i) => {
          const speed = 4 + (i % 5) * 3;
          const x = (1920 - ((frame * speed + i * 110) % 2100)) + 80;
          const y = (i * 59) % 780;
          const len = speed * 4;
          return (
            <line
              key={i}
              x1={x}
              y1={y}
              x2={x + len}
              y2={y}
              stroke={i % 4 === 0 ? "#38BDF8" : "#FFFFFF"}
              strokeWidth={i % 3 === 0 ? 3 : 1.5}
              opacity={0.8}
            />
          );
        })}

        {/* Marco de parabrisas panorámico curvo */}
        <path
          d="M 0 0 L 320 0 L 260 780 L 0 850 Z"
          fill="#0F172A"
          stroke="#000000"
          strokeWidth="6"
        />
        <path
          d="M 1920 0 L 1600 0 L 1660 780 L 1920 850 Z"
          fill="#0F172A"
          stroke="#000000"
          strokeWidth="6"
        />
        <path
          d="M 260 780 Q 960 730 1660 780 L 1920 1080 L 0 1080 Z"
          fill="#0F172A"
          stroke="#000000"
          strokeWidth="6"
        />

        {/* Consola de mandos inferior con displays y controles */}
        <rect x="360" y="820" width="1200" height="260" rx="16" fill="#1E293B" stroke="#000000" strokeWidth="6" />

        {/* HUD Holográfico en el parabrisas */}
        <g opacity={0.75}>
          {/* Círculo central de retículo de vuelo */}
          <circle cx="960" cy="420" r="160" fill="none" stroke="#38BDF8" strokeWidth="2" strokeDasharray="16 10" />
          <circle cx="960" cy="420" r="8" fill="#38BDF8" />
          <line x1="760" y1="420" x2="860" y2="420" stroke="#38BDF8" strokeWidth="3" />
          <line x1="1060" y1="420" x2="1160" y2="420" stroke="#38BDF8" strokeWidth="3" />
          <line x1="960" y1="220" x2="960" y2="320" stroke="#38BDF8" strokeWidth="3" />
          <line x1="960" y1="520" x2="960" y2="620" stroke="#38BDF8" strokeWidth="3" />

          {/* Medidor de vector de luz c */}
          <rect x="420" y="860" width="280" height="80" rx="10" fill="#020617" stroke="#38BDF8" strokeWidth="3" />
          <text x="440" y="905" fill="#38BDF8" fontSize="24" fontWeight="bold" fontFamily="monospace">
            PROPULSIÓN: ON
          </text>
          <text x="440" y="930" fill="#94A3B8" fontSize="16" fontFamily="monospace">
            CAMPO RELATIVISTA ACTIVO
          </text>
        </g>
      </svg>
    </div>
  );
};

/** Túnel Óptico Relativista (Aberración de la luz + Corrimiento Doppler al azul y gamma) */
const TunelRelativistaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pulse = Math.sin(frame / 8) * 0.2 + 0.8;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#020617] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          {/* Gradiente Doppler: Borde exterior cálido (CMB), anillo medio azul, centro negro de rayos gamma */}
          <radialGradient id="dopplerGradient" cx="50%" cy="50%" r="55%">
            <stop offset="0%" stopColor="#000000" />
            <stop offset="18%" stopColor="#4C1D95" />
            <stop offset="40%" stopColor="#2563EB" />
            <stop offset="65%" stopColor="#06B6D4" />
            <stop offset="85%" stopColor="#EA580C" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#7F1D1D" stopOpacity="0.4" />
          </radialGradient>
        </defs>

        <rect width="1920" height="1080" fill="url(#dopplerGradient)" />

        {/* Rayos de estrellas comprimiéndose hacia el centro (aberración frontal) */}
        {Array.from({ length: 48 }).map((_, i) => {
          const angle = (i * 360) / 48;
          const rad = (angle * Math.PI) / 180;
          const startDist = 900 - ((frame * 12 + i * 40) % 850);
          const endDist = Math.max(80, startDist - 120);

          const x1 = 960 + Math.cos(rad) * startDist;
          const y1 = 540 + Math.sin(rad) * startDist;
          const x2 = 960 + Math.cos(rad) * endDist;
          const y2 = 540 + Math.sin(rad) * endDist;

          return (
            <line
              key={i}
              x1={x1}
              y1={y1}
              x2={x2}
              y2={y2}
              stroke={i % 3 === 0 ? "#67E8F9" : "#C084FC"}
              strokeWidth={Math.max(1.5, 4 - (endDist / 300))}
              opacity={0.85 * pulse}
            />
          );
        })}

        {/* Cono central: Centro oscuro de radiación gamma invisible */}
        <circle cx="960" cy="540" r="140" fill="#000000" stroke="#7C3AED" strokeWidth="4" strokeDasharray="14 8" />
        <circle cx="960" cy="540" r="80" fill="#000000" />

        {/* Retículo de advertencia de rayos gamma */}
        <text
          x="960"
          y="545"
          fill="#C084FC"
          fontSize="18"
          fontWeight="black"
          textAnchor="middle"
          letterSpacing="4"
        >
          [ ZONA GAMMA ]
        </text>
      </svg>
    </div>
  );
};

/** 1. Salón de Billar Victoriano (1860s) - Mesa de paño verde y lámparas de gas */
const SalonBillarStage: React.FC<{ frame: number }> = ({ frame }) => {
  const flicker = 0.95 + Math.sin(frame / 6) * 0.05;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="wallWood" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E140A" />
            <stop offset="60%" stopColor="#2E1A0F" />
            <stop offset="100%" stopColor="#150B05" />
          </linearGradient>
          <linearGradient id="billiardFelt" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#065F46" />
            <stop offset="70%" stopColor="#047857" />
            <stop offset="100%" stopColor="#064E3B" />
          </linearGradient>
          <radialGradient id="lampCone" cx="50%" cy="0%" r="90%">
            <stop offset="0%" stopColor="#FEF08A" stopOpacity="0.45" />
            <stop offset="50%" stopColor="#FBBF24" stopOpacity="0.15" />
            <stop offset="100%" stopColor="transparent" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Pared victoriana de madera oscura con molduras */}
        <rect x="0" y="0" width="1920" height="1080" fill="url(#wallWood)" />
        {Array.from({ length: 8 }).map((_, i) => (
          <g key={i}>
            <rect x={i * 240 + 20} y="120" width="200" height="320" rx="8" fill="#1C1109" stroke="#3D2415" strokeWidth="4" />
            <rect x={i * 240 + 35} y="135" width="170" height="290" rx="4" fill="#150B05" stroke="#4A2D19" strokeWidth="2" />
          </g>
        ))}
        {/* Moldura de zócalo horizontal */}
        <line x1="0" y1="460" x2="1920" y2="460" stroke="#78350F" strokeWidth="12" />
        <line x1="0" y1="472" x2="1920" y2="472" stroke="#451A03" strokeWidth="6" />

        {/* Lámparas de gas victorianas con tulipas verdes */}
        {[500, 960, 1420].map((lx, idx) => (
          <g key={idx}>
            {/* Cadena y soporte de latón */}
            <line x1={lx} y1="0" x2={lx} y2="110" stroke="#D97706" strokeWidth="5" />
            <path d={`M ${lx - 80} 150 L ${lx - 40} 110 L ${lx + 40} 110 L ${lx + 80} 150 Z`} fill="#047857" stroke="#10B981" strokeWidth="4" />
            <ellipse cx={lx} cy="150" rx="80" ry="16" fill="#FDE047" opacity={0.9 * flicker} />
            {/* Cono de luz cálida sobre la mesa */}
            <polygon points={`${lx - 70},155 ${lx + 70},155 ${lx + 320},900 ${lx - 320},900`} fill="url(#lampCone)" opacity={flicker} />
          </g>
        ))}

        {/* Mesa de Billar monumental en perspectiva */}
        <g id="mesa_billar">
          {/* Faldón de madera de caoba */}
          <polygon points="120,680 1800,680 1880,1080 40,1080" fill="#2E1005" stroke="#451A03" strokeWidth="8" />
          <polygon points="150,650 1770,650 1850,1020 70,1020" fill="#78350F" stroke="#92400E" strokeWidth="6" />
          {/* Paño verde esmeralda */}
          <polygon points="190,660 1730,660 1800,990 120,990" fill="url(#billiardFelt)" stroke="#064E3B" strokeWidth="6" />
          {/* Troneras doradas de latón */}
          {[
            [190, 660],
            [960, 660],
            [1730, 660],
            [120, 990],
            [960, 990],
            [1800, 990],
          ].map(([tx, ty], i) => (
            <circle key={i} cx={tx} cy={ty} r="24" fill="#000000" stroke="#F59E0B" strokeWidth="5" />
          ))}
          {/* Bolas de billar sobre la mesa */}
          <circle cx="820" cy="810" r="18" fill="#F8FAFC" stroke="#000000" strokeWidth="3" />
          <circle cx="1040" cy="780" r="18" fill="#EF4444" stroke="#000000" strokeWidth="3" />
          <circle cx="1120" cy="850" r="18" fill="#F59E0B" stroke="#000000" strokeWidth="3" />
        </g>
      </svg>
    </div>
  );
};

/** 2. Taller Artesanal de Inventor (John Wesley Hyatt, 1869) */
const TallerInventorStage: React.FC<{ frame: number }> = ({ frame }) => {
  const bubbleY = (frame * 3) % 40;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#181109] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="workshopBg" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E140A" />
            <stop offset="60%" stopColor="#2A180C" />
            <stop offset="100%" stopColor="#140B05" />
          </linearGradient>
        </defs>
        <rect x="0" y="0" width="1920" height="1080" fill="url(#workshopBg)" />

        {/* Ventana industrial victoriana al fondo izquierdo */}
        <rect x="90" y="120" width="220" height="280" rx="8" fill="#1E293B" stroke="#451A03" strokeWidth="8" />
        <line x1="200" y1="120" x2="200" y2="400" stroke="#451A03" strokeWidth="6" />
        <line x1="90" y1="260" x2="310" y2="260" stroke="#451A03" strokeWidth="6" />

        {/* Estanterías con frascos y matraces químicos */}
        <rect x="380" y="220" width="520" height="18" fill="#78350F" stroke="#451A03" strokeWidth="4" />
        <rect x="380" y="360" width="520" height="18" fill="#78350F" stroke="#451A03" strokeWidth="4" />

        {/* Boticas y retortas en la estantería */}
        <g transform="translate(430, 155)">
          <path d="M 0 60 L 0 25 L 15 0 L 35 0 L 50 25 L 50 60 Z" fill="#0284C7" opacity="0.8" stroke="#38BDF8" strokeWidth="3" />
          <circle cx="25" cy={45 - bubbleY * 0.7} r="3" fill="#BAE6FD" />
        </g>
        <g transform="translate(560, 245)">
          <rect x="0" y="0" width="76" height="110" rx="8" fill="#78350F" stroke="#B45309" strokeWidth="4" />
          <text x="38" y="62" fill="#FEF08A" fontSize="14" fontWeight="bold" textAnchor="middle">ÁCIDO</text>
        </g>
        <g transform="translate(700, 255)">
          <rect x="0" y="0" width="90" height="100" rx="8" fill="#E2E8F0" stroke="#475569" strokeWidth="4" />
          <text x="45" y="56" fill="#0F172A" fontSize="13" fontWeight="900" textAnchor="middle">ALCANFOR</text>
        </g>

        {/* Campana extractora de cobre sobre la zona de prensado derecha */}
        <polygon points="1140,0 1460,0 1540,190 1060,190" fill="#451A03" stroke="#78350F" strokeWidth="6" />
        <rect x="1250" y="0" width="100" height="90" fill="#2E1B10" stroke="#78350F" strokeWidth="5" />

        {/* Mesa/suelo de trabajo de madera rústica */}
        <rect x="0" y="780" width="1920" height="300" fill="#2E1B10" stroke="#451A03" strokeWidth="8" />
        <line x1="0" y1="792" x2="1920" y2="792" stroke="#78350F" strokeWidth="4" />

        {/* Sacos de algodón de celulosa apoyados limpiamente sobre el banco izquierdo */}
        <ellipse cx="170" cy="740" rx="85" ry="52" fill="#F8FAFC" stroke="#000000" strokeWidth="5" />
        <ellipse cx="290" cy="748" rx="92" ry="56" fill="#F1F5F9" stroke="#000000" strokeWidth="5" />
        <text x="235" y="752" fill="#0F172A" fontSize="20" fontWeight="900" textAnchor="middle">ALGODÓN</text>
      </svg>
    </div>
  );
};

/** 3. Saloon del Salvaje Oeste (1870s) */
const SaloonOesteStage: React.FC<{ frame: number }> = ({ frame }) => {
  const lanternSwing = Math.sin(frame / 12) * 5;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#29170D] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Tablones de madera desgastada */}
        {Array.from({ length: 18 }).map((_, i) => (
          <line key={i} x1="0" y1={i * 60} x2="1920" y2={i * 60} stroke="#1A0E07" strokeWidth="4" />
        ))}
        {/* Puertas vaqueras batientes en el centro */}
        <g transform="translate(960, 420)">
          <rect x="-240" y="-160" width="200" height="320" rx="8" fill="#582F16" stroke="#2B150A" strokeWidth="7" />
          <rect x="40" y="-160" width="200" height="320" rx="8" fill="#582F16" stroke="#2B150A" strokeWidth="7" />
          {/* Rejillas clásicas de saloon */}
          {[-80, -40, 0, 40, 80].map((ly, j) => (
            <g key={j}>
              <line x1="-220" y1={ly} x2="-60" y2={ly} stroke="#2B150A" strokeWidth="5" />
              <line x1="60" y1={ly} x2="220" y2={ly} stroke="#2B150A" strokeWidth="5" />
            </g>
          ))}
        </g>

        {/* Linterna de queroseno balanceándose */}
        <g transform={`translate(480, 140) rotate(${lanternSwing} 0 0)`}>
          <line x1="0" y1="-80" x2="0" y2="0" stroke="#000000" strokeWidth="4" />
          <rect x="-30" y="0" width="60" height="80" rx="6" fill="#FBBF24" opacity="0.85" stroke="#000000" strokeWidth="5" />
          <circle cx="0" cy="40" r="14" fill="#FEF08A" />
        </g>

        {/* Barra de bar de roble */}
        <rect x="0" y="740" width="1920" height="340" fill="#3D1F0E" stroke="#1F0E05" strokeWidth="8" />
        <rect x="0" y="720" width="1920" height="30" fill="#78350F" stroke="#451A03" strokeWidth="5" />
      </svg>
    </div>
  );
};

/** 4. Espacio de Arquitectura Molecular (Blueprint Técnico Azul/Cian) */
const EspacioMolecularStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B1528] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Cuadrícula Blueprint técnica */}
        <defs>
          <pattern id="blueGrid" width="60" height="60" patternUnits="userSpaceOnUse">
            <rect width="60" height="60" fill="none" stroke="#1E293B" strokeWidth="1.5" />
            <circle cx="30" cy="30" r="2" fill="#0284C7" opacity="0.4" />
          </pattern>
        </defs>
        <rect x="0" y="0" width="1920" height="1080" fill="url(#blueGrid)" />

        {/* Anillos aromáticos de carbono (benceno/fenol) sutiles en el perímetro superior */}
        {[
          [240, 210],
          [960, 170],
          [1680, 210],
        ].map(([hx, hy], idx) => (
          <g key={idx} transform={`translate(${hx}, ${hy}) rotate(${(frame * 1.5 + idx * 45) % 360} 0 0)`} opacity="0.45">
            <polygon
              points="0,-42 36,-20 36,20 0,42 -36,20 -36,-20"
              fill="none"
              stroke="#0284C7"
              strokeWidth="3.5"
              strokeDasharray="8 4"
            />
            <circle cx="0" cy="0" r="22" fill="none" stroke="#38BDF8" strokeWidth="2.5" />
          </g>
        ))}

        {/* Plataforma/mesa de trabajo blueprint para pruebas de monómeros y polímeros */}
        <rect x="0" y="790" width="1920" height="290" fill="#081020" stroke="#0284C7" strokeWidth="6" />
        <line x1="120" y1="815" x2="1800" y2="815" stroke="#1E293B" strokeWidth="3" strokeDasharray="16 8" />

        {/* Rótulo técnico en marca de agua */}
        <text x="960" y="875" fill="#0284C7" fontSize="24" fontWeight="900" textAnchor="middle" opacity="0.35" letterSpacing="6">
          LABORATORIO DE ARQUITECTURA MACROMOLECULAR
        </text>
      </svg>
    </div>
  );
};

/** 5. Laboratorio Industrial de Baekeland (Yonkers, Nueva York, 1907) */
const LaboratorioBaekelandStage: React.FC<{ frame: number }> = ({ frame }) => {
  const steamPuff = Math.sin(frame / 5) * 8;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Pared de ladrillo oscuro industrial */}
        <rect x="0" y="0" width="1920" height="1080" fill="#111827" />
        {Array.from({ length: 12 }).map((_, i) => (
          <line key={i} x1="0" y1={i * 70} x2="1920" y2={i * 70} stroke="#1E293B" strokeWidth="2" />
        ))}

        {/* Tuberías maestras de cobre y manómetros murales */}
        <path d="M 0 170 L 1920 170" stroke="#B45309" strokeWidth="18" fill="none" />
        <path d="M 0 170 L 1920 170" stroke="#F59E0B" strokeWidth="4" fill="none" opacity="0.5" />
        <path d="M 1120 170 L 1120 420" stroke="#B45309" strokeWidth="16" fill="none" />
        <path d="M 1420 170 L 1420 420" stroke="#B45309" strokeWidth="16" fill="none" />

        {/* Estación auxiliar de reactivos a la izquierda */}
        <rect x="100" y="340" width="360" height="16" fill="#475569" stroke="#000000" strokeWidth="4" />
        <rect x="140" y="260" width="54" height="80" rx="6" fill="#78350F" stroke="#000000" strokeWidth="4" />
        <text x="167" y="306" fill="#FEF08A" fontSize="11" fontWeight="900" textAnchor="middle">FENOL</text>
        <rect x="220" y="250" width="76" height="90" rx="6" fill="#065F46" stroke="#000000" strokeWidth="4" />
        <text x="258" y="302" fill="#A7F3D0" fontSize="10" fontWeight="900" textAnchor="middle">FORMOL</text>

        {/* Plataforma de acero reforzado para el reactor */}
        <rect x="880" y="730" width="680" height="55" rx="6" fill="#334155" stroke="#000000" strokeWidth="6" />
        <rect x="0" y="785" width="1920" height="295" fill="#1E293B" stroke="#0F172A" strokeWidth="8" />

        {/* Vapor tenue en las válvulas superiores de cobre */}
        <circle cx={1120 + steamPuff} cy="145" r="18" fill="#E2E8F0" opacity="0.25" />
        <circle cx={1420 - steamPuff} cy="140" r="22" fill="#E2E8F0" opacity="0.2" />
      </svg>
    </div>
  );
};

/** 6. Infraestructura de Red Eléctrica Urbana (1910-1920s) */
const InfraestructuraElectricaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const spark = (frame * 18) % 1920;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#090D16] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Cielo nocturno con gradiente crepuscular */}
        <defs>
          <linearGradient id="nightSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0B132B" />
            <stop offset="70%" stopColor="#1C2541" />
            <stop offset="100%" stopColor="#3A506B" />
          </linearGradient>
        </defs>
        <rect x="0" y="0" width="1920" height="1080" fill="url(#nightSky)" />

        {/* Silueta de rascacielos al horizonte con ventanas iluminadas */}
        {Array.from({ length: 14 }).map((_, i) => (
          <g key={i}>
            <rect x={i * 140} y={620 - (i % 5) * 60} width="120" height="500" fill="#0B111E" stroke="#1E293B" strokeWidth="3" />
            {Array.from({ length: 6 }).map((_, j) => (
              <rect key={j} x={i * 140 + 20 + (j % 3) * 30} y={660 - (i % 5) * 60 + Math.floor(j / 3) * 50} width="16" height="24" fill="#FDE047" opacity={0.7} />
            ))}
          </g>
        ))}

        {/* Postes de luz de madera con crucetas y aisladores de baquelita */}
        {[380, 1180].map((px, idx) => (
          <g key={idx}>
            <rect x={px - 20} y="160" width="40" height="920" fill="#451A03" stroke="#000000" strokeWidth="6" />
            {/* Cruceta horizontal */}
            <rect x={px - 220} y="240" width="440" height="26" fill="#78350F" stroke="#000000" strokeWidth="5" />
            {/* Aisladores cilíndricos oscuros de baquelita */}
            {[-180, -60, 60, 180].map((ix, k) => (
              <g key={k} transform={`translate(${px + ix}, 210)`}>
                <rect x="-14" y="0" width="28" height="30" rx="4" fill="#1C1917" stroke="#000000" strokeWidth="3" />
                <circle cx="0" cy="0" r="16" fill="#292524" stroke="#000000" strokeWidth="3" />
              </g>
            ))}
          </g>
        ))}

        {/* Líneas de alta tensión con chispas de corriente fluyendo */}
        <path d="M 0 210 Q 590 320 1180 210 Q 1550 300 1920 210" fill="none" stroke="#0284C7" strokeWidth="7" />
        <path d="M 0 250 Q 590 360 1180 250 Q 1550 340 1920 250" fill="none" stroke="#38BDF8" strokeWidth="5" />
        {/* Pulso de energía eléctrica recorriendo los cables */}
        <circle cx={spark} cy={230 + Math.sin(spark / 200) * 40} r="10" fill="#FFE600" opacity="0.9" />
      </svg>
    </div>
  );
};

/** 7. Galería de Diseño de la Era del Plástico (Art Déco / Masas) */
const GaleriaDisenoRetroStage: React.FC<{ frame: number }> = () => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#F1F5F9] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Fondo de museo de diseño moderno limpio */}
        <rect x="0" y="0" width="1920" height="1080" fill="#F8FAFC" />
        {/* Suelo cuadriculado estilo galería */}
        <polygon points="0,780 1920,780 1920,1080 0,1080" fill="#E2E8F0" stroke="#94A3B8" strokeWidth="4" />

        {/* Pedestales de exhibición */}
        {[380, 820, 1260, 1680].map((pedX, idx) => (
          <g key={idx}>
            <rect x={pedX - 110} y="620" width="220" height="240" rx="6" fill="#FFFFFF" stroke="#000000" strokeWidth="6" />
            <polygon points={`${pedX - 110},620 ${pedX - 80},590 ${pedX + 140},590 ${pedX + 110},620`} fill="#CBD5E1" stroke="#000000" strokeWidth="4" />
          </g>
        ))}

        {/* Banner de Árbol Genealógico de Polímeros */}
        <rect x="240" y="80" width="1440" height="160" rx="16" fill="#1E293B" stroke="#000000" strokeWidth="7" />
        <text x="960" y="145" fill="#FFE600" fontSize="36" fontWeight="900" textAnchor="middle" letterSpacing="3">
          LA ERA SINTÉTICA: BAQUELITA (1907) → NYLON (1935) → POLIETILENO (1939)
        </text>
        <text x="960" y="195" fill="#94A3B8" fontSize="20" fontWeight="bold" textAnchor="middle">
          DE LA CONSERVACIÓN BIOLÓGICA A LA PRODUCCIÓN INFINITA EN MASA
        </text>
      </svg>
    </div>
  );
};

/** 8. Basurero y Columna Geológica del Antropoceno (Plastiglomerados) */
const BasureroEstratigraficoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const glint = (frame * 4) % 1920;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1C1917] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Estrato 1: Capa profunda jurásica con fósiles de dinosaurio */}
        <rect x="0" y="780" width="1920" height="300" fill="#292524" stroke="#000000" strokeWidth="6" />
        <path d="M 240 880 Q 340 850 440 920 Q 540 880 620 940" stroke="#78716C" strokeWidth="10" strokeLinecap="round" fill="none" />
        <circle cx="280" cy="880" r="18" fill="#A8A29E" />
        <text x="380" y="990" fill="#78716C" fontSize="24" fontWeight="900">ESTRATO JURÁSICO (-150M AÑOS)</text>

        {/* Estrato 2: Capa pleistocénica con herramientas de piedra */}
        <rect x="0" y="520" width="1920" height="260" fill="#44403C" stroke="#000000" strokeWidth="6" />
        <polygon points="1240,620 1280,590 1310,650 1250,670" fill="#78716C" stroke="#000000" strokeWidth="4" />
        <text x="1200" y="730" fill="#A8A29E" fontSize="24" fontWeight="900">ESTRATO LÍTICO (-50.000 AÑOS)</text>

        {/* Estrato 3: La fina capa de Plastiglomerados del Antropoceno (Colorida, brillante y permanente) */}
        <rect x="0" y="280" width="1920" height="240" fill="#1C1917" stroke="#EF4444" strokeWidth="6" strokeDasharray="14 8" />
        {/* Restos compactados de botellas, popotes y tapas multicolores */}
        {Array.from({ length: 28 }).map((_, i) => (
          <g key={i}>
            <rect
              x={i * 68 + 20}
              y={340 + (i % 4) * 28}
              width="45"
              height="20"
              rx="4"
              fill={["#EF4444", "#38BDF8", "#FBBF24", "#10B981", "#EC4899", "#8B5CF6"][i % 6]}
              stroke="#000000"
              strokeWidth="3"
            />
            <circle cx={i * 68 + 50} cy={350 + (i % 4) * 28} r="6" fill="#FFFFFF" opacity="0.6" />
          </g>
        ))}
        {/* Destello de microplásticos fluorescentes */}
        <circle cx={glint} cy={400} r="8" fill="#67E8F9" opacity="0.9" />
        <text x="960" y="320" fill="#EF4444" fontSize="32" fontWeight="900" textAnchor="middle" letterSpacing="4">
          CAPA ANTROPOGÉNICA: PLASTIGLOMERADOS Y MICROPLÁSTICOS (INMORTAL)
        </text>
      </svg>
    </div>
  );
};

/** 9. Sabana Africana al Atardecer con Elefantes en Libertad */
const SabanaAfricanaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const marchX = (frame * 1.5) % 1920;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#451A03] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="savannaSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#7C2D12" />
            <stop offset="40%" stopColor="#EA580C" />
            <stop offset="70%" stopColor="#F59E0B" />
            <stop offset="100%" stopColor="#FEF08A" />
          </linearGradient>
        </defs>
        {/* Cielo crepuscular naranja africano */}
        <rect x="0" y="0" width="1920" height="1080" fill="url(#savannaSky)" />

        {/* Sol gigante en el horizonte */}
        <circle cx="960" cy="560" r="160" fill="#FEF08A" opacity="0.9" />

        {/* Siluetas de Acacias africanas */}
        {[240, 1540].map((ax, idx) => (
          <g key={idx} transform={`translate(${ax}, 600)`}>
            <path d="M 0 180 Q -10 60 -40 0 Q -20 -40 -120 -60 Q 0 -90 120 -60 Q 20 -40 40 0 Q 10 60 0 180 Z" fill="#1C1917" />
          </g>
        ))}

        {/* Llanura de la sabana en silueta negra */}
        <path d="M 0 740 Q 480 720 960 740 Q 1440 760 1920 740 L 1920 1080 L 0 1080 Z" fill="#1C1917" />

        {/* Manada de elefantes caminando en paz en silueta */}
        <g id="manada_elefantes" transform={`translate(${1920 - marchX}, 670)`}>
          {/* Elefante grande */}
          <ellipse cx="0" cy="0" rx="65" ry="50" fill="#0C0A09" />
          <circle cx="50" cy="-20" r="30" fill="#0C0A09" />
          {/* Trompa */}
          <path d="M 70 -15 Q 90 0 85 30" stroke="#0C0A09" strokeWidth="16" fill="none" strokeLinecap="round" />
          {/* Colmillo blanco visible y libre */}
          <path d="M 68 -5 Q 85 10 92 0" stroke="#FEF3C7" strokeWidth="6" fill="none" strokeLinecap="round" />
          {/* Patas */}
          <rect x="-45" y="30" width="18" height="50" rx="6" fill="#0C0A09" />
          <rect x="-15" y="30" width="18" height="50" rx="6" fill="#0C0A09" />
          <rect x="15" y="30" width="18" height="50" rx="6" fill="#0C0A09" />
          <rect x="40" y="30" width="18" height="50" rx="6" fill="#0C0A09" />

          {/* Elefante bebé siguiéndole */}
          <g transform="translate(-110, 25) scale(0.6)">
            <ellipse cx="0" cy="0" rx="65" ry="50" fill="#0C0A09" />
            <circle cx="50" cy="-20" r="30" fill="#0C0A09" />
            <path d="M 70 -15 Q 90 0 85 25" stroke="#0C0A09" strokeWidth="14" fill="none" strokeLinecap="round" />
            <rect x="-45" y="30" width="18" height="50" rx="6" fill="#0C0A09" />
            <rect x="35" y="30" width="18" height="50" rx="6" fill="#0C0A09" />
          </g>
        </g>
      </svg>
    </div>
  );
};

/** 10. Cantera y Puente de Piedra Clásico (Ingeniería de Mampostería y Gravedad) */
const CanteraPuentePiedraStage: React.FC<{ frame: number }> = ({ frame }) => {
  const riverShift = (frame * 2.5) % 160;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="quarrySky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0B132B" />
            <stop offset="55%" stopColor="#1E293B" />
            <stop offset="100%" stopColor="#334155" />
          </linearGradient>
        </defs>
        <rect width="1920" height="1080" fill="url(#quarrySky)" />

        {/* Montañas de cantera escalonadas al fondo */}
        <polygon points="0,680 280,420 560,580 920,390 1340,560 1680,410 1920,540 1920,780 0,780" fill="#1E293B" stroke="#0F172A" strokeWidth="5" />

        {/* Gran acueducto / puente de piedra en segundo plano */}
        <g opacity="0.55">
          <rect x="120" y="470" width="1680" height="36" fill="#475569" stroke="#0F172A" strokeWidth="4" />
          {[240, 560, 880, 1200, 1520].map((archX, i) => (
            <path
              key={i}
              d={`M ${archX - 110} 740 L ${archX - 110} 506 L ${archX + 110} 506 L ${archX + 110} 740 L ${archX + 65} 740 A 65 80 0 0 0 ${archX - 65} 740 Z`}
              fill="#334155"
              stroke="#0F172A"
              strokeWidth="4"
            />
          ))}
        </g>

        {/* Río caudaloso bajo los arcos */}
        <rect x="0" y="710" width="1920" height="75" fill="#0369A1" />
        {Array.from({ length: 12 }).map((_, i) => (
          <line
            key={i}
            x1={(i * 180 + riverShift) % 1920}
            y1={735 + (i % 2) * 22}
            x2={((i * 180 + riverShift) % 1920) + 90}
            y2={735 + (i % 2) * 22}
            stroke="#38BDF8"
            strokeWidth="4"
            strokeLinecap="round"
            opacity="0.55"
          />
        ))}

        {/* Explanada de piedra labrada en primer plano donde actúan los personajes */}
        <rect x="0" y="780" width="1920" height="300" fill="#1E293B" stroke="#000000" strokeWidth="8" />
        {Array.from({ length: 10 }).map((_, i) => (
          <line key={i} x1={i * 200} y1="780" x2={i * 200 - 80} y2="1080" stroke="#334155" strokeWidth="4" />
        ))}
        <line x1="0" y1="860" x2="1920" y2="860" stroke="#334155" strokeWidth="4" />
      </svg>
    </div>
  );
};

/** 11. Arsenal Naval de Venecia y Estudio Renacentista de Galileo (1638) */
const ArsenalVeneciaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const waterWave = Math.sin(frame / 10) * 10;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#141824] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="veniceSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0F172A" />
            <stop offset="65%" stopColor="#1E293B" />
            <stop offset="100%" stopColor="#334155" />
          </linearGradient>
        </defs>
        <rect width="1920" height="1080" fill="url(#veniceSky)" />

        {/* Arcadas de ladrillo renacentista del Arsenal de Venecia */}
        {[180, 620, 1460].map((ax, idx) => (
          <g key={idx} opacity="0.5">
            <rect x={ax - 150} y="160" width="300" height="580" fill="#451A03" stroke="#000000" strokeWidth="5" />
            <path d={`M ${ax - 110} 740 L ${ax - 110} 340 A 110 110 0 0 1 ${ax + 110} 340 L ${ax + 110} 740 Z`} fill="#0F172A" stroke="#78350F" strokeWidth="6" />
          </g>
        ))}

        {/* Pizarra de geometría clásica renacentista (L vs L² vs L³) a la izquierda */}
        <g transform="translate(110, 210)" opacity="0.85">
          <rect width="310" height="210" rx="10" fill="#1C1917" stroke="#B45309" strokeWidth="7" />
          <text x="155" y="42" fill="#FDE68A" fontSize="20" fontWeight="900" textAnchor="middle" fontFamily="serif">
            DISCORSI (1638)
          </text>
          <rect x="45" y="85" width="42" height="42" fill="none" stroke="#38BDF8" strokeWidth="3.5" />
          <rect x="115" y="65" width="84" height="84" fill="none" stroke="#F59E0B" strokeWidth="3.5" />
          <text x="245" y="100" fill="#FDE68A" fontSize="22" fontWeight="bold" textAnchor="middle">
            A ∝ L²
          </text>
          <text x="245" y="138" fill="#EF4444" fontSize="22" fontWeight="bold" textAnchor="middle">
            M ∝ L³
          </text>
        </g>

        {/* Canal veneciano al fondo y muelle de piedra */}
        <rect x="0" y="715" width="1920" height="65" fill="#0C4A6E" />
        <path
          d={`M 0 745 Q 480 ${735 + waterWave} 960 745 T 1920 745`}
          fill="none"
          stroke="#38BDF8"
          strokeWidth="3"
          opacity="0.5"
        />

        {/* Muelle de losas de piedra veneciana */}
        <rect x="0" y="780" width="1920" height="300" fill="#292524" stroke="#000000" strokeWidth="8" />
        <line x1="0" y1="795" x2="1920" y2="795" stroke="#57534E" strokeWidth="5" />
      </svg>
    </div>
  );
};

/** 12. Estrecho de Tacoma Narrows (1940) — Cañón Costero y Viento Aerodinámico */
const EstrechoTacomaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const windOffset = (frame * 9) % 1920;
  const waveShift = Math.sin(frame / 7) * 14;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="stormSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#090D16" />
            <stop offset="55%" stopColor="#1E293B" />
            <stop offset="100%" stopColor="#334155" />
          </linearGradient>
        </defs>
        <rect width="1920" height="1080" fill="url(#stormSky)" />

        {/* Corrientes de viento de 68 km/h cruzando el cielo del estrecho */}
        {[180, 310, 440].map((wy, i) => (
          <path
            key={i}
            d={`M ${(windOffset + i * 620) % 1920 - 300} ${wy} Q ${(windOffset + i * 620) % 1920 - 150} ${wy - 22} ${(windOffset + i * 620) % 1920} ${wy} T ${(windOffset + i * 620) % 1920 + 260} ${wy}`}
            fill="none"
            stroke="#38BDF8"
            strokeWidth="3"
            opacity="0.32"
            strokeLinecap="round"
          />
        ))}

        {/* Acantilados costeros de Washington a ambos lados del estrecho */}
        <polygon points="0,430 420,490 580,720 0,720" fill="#1E293B" stroke="#0F172A" strokeWidth="5" />
        <polygon points="1920,410 1440,480 1280,720 1920,720" fill="#1E293B" stroke="#0F172A" strokeWidth="5" />

        {/* Aguas agitadas de Puget Sound */}
        <rect x="0" y="690" width="1920" height="95" fill="#0369A1" />
        <path
          d={`M 0 730 Q 320 ${712 + waveShift} 640 730 T 1280 730 T 1920 730`}
          fill="none"
          stroke="#7DD3FC"
          strokeWidth="4"
          opacity="0.65"
        />

        {/* Mirador de hormigón costero en primer plano */}
        <rect x="0" y="780" width="1920" height="300" fill="#1E293B" stroke="#000000" strokeWidth="8" />
        <line x1="0" y1="745" x2="1920" y2="745" stroke="#475569" strokeWidth="6" />
      </svg>
    </div>
  );
};

/** 13. Metrópoli de Rascacielos y Explanada de Ingeniería Estructural Moderna (Sin postes de luz) */
const MetropoliRascacielosStage: React.FC<{ frame: number }> = ({ frame }) => {
  const beaconOpacity = 0.4 + Math.sin(frame / 10) * 0.5;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#090D16] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="metroSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#060B19" />
            <stop offset="60%" stopColor="#0F172A" />
            <stop offset="100%" stopColor="#1E293B" />
          </linearGradient>
          <pattern id="engGrid" width="80" height="80" patternUnits="userSpaceOnUse">
            <path d="M 80 0 L 0 0 0 80" fill="none" stroke="#1E293B" strokeWidth="1.5" opacity="0.55" />
          </pattern>
        </defs>
        <rect width="1920" height="1080" fill="url(#metroSky)" />
        <rect width="1920" height="780" fill="url(#engGrid)" />

        {/* Silueta panorámica de megatorres modernas al fondo (lejanas, limpias, sin cables cruzando) */}
        {[
          { x: 110, w: 110, h: 420 },
          { x: 260, w: 130, h: 520 },
          { x: 430, w: 95, h: 360 },
          { x: 1380, w: 125, h: 490 },
          { x: 1540, w: 140, h: 580 },
          { x: 1710, w: 115, h: 430 },
        ].map((b, idx) => (
          <g key={idx} opacity="0.65">
            <rect
              x={b.x}
              y={780 - b.h}
              width={b.w}
              height={b.h}
              fill="#0F172A"
              stroke="#334155"
              strokeWidth="3"
            />
            {/* Entramado diagonal de acero sutil en las fachadas */}
            <line x1={b.x} y1={780 - b.h} x2={b.x + b.w} y2={780 - b.h + 140} stroke="#1E293B" strokeWidth="2.5" />
            <line x1={b.x + b.w} y1={780 - b.h} x2={b.x} y2={780 - b.h + 140} stroke="#1E293B" strokeWidth="2.5" />
            {/* Baliza roja anticolisión en las agujas */}
            <circle cx={b.x + b.w / 2} cy={780 - b.h - 12} r="5" fill="#EF4444" opacity={beaconOpacity} />
          </g>
        ))}

        {/* Explanada de ingeniería de acero y hormigón en primer plano */}
        <rect x="0" y="780" width="1920" height="300" fill="#111827" stroke="#0284C7" strokeWidth="6" />
        <line x1="0" y1="796" x2="1920" y2="796" stroke="#1E293B" strokeWidth="3" strokeDasharray="20 10" />
      </svg>
    </div>
  );
};

/** 14. Metrópoli Nocturna Bajo Intenso Resplandor Celeste (Skyglow Naranja / Cero Estrellas) */
const MetropoliNocheResplandorStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pulseSky = 0.85 + Math.sin(frame * 0.14) * 0.12;
  const beamShift = Math.sin(frame * 0.16) * 40;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1A0B05] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          {/* Cúpula de resplandor lechoso urbano (Skyglow anaranjado artificial) */}
          <radialGradient id="skyglowDome" cx="50%" cy="85%" r="70%">
            <stop offset="0%" stopColor="#EA580C" stopOpacity="0.85" />
            <stop offset="35%" stopColor="#B45309" stopOpacity="0.7" />
            <stop offset="70%" stopColor="#451A03" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#0C0A09" stopOpacity="1" />
          </radialGradient>
          <linearGradient id="beamGradient" x1="0" y1="1" x2="0" y2="0">
            <stop offset="0%" stopColor="#FDE047" stopOpacity="0.45" />
            <stop offset="60%" stopColor="#F59E0B" stopOpacity="0.2" />
            <stop offset="100%" stopColor="#B45309" stopOpacity="0" />
          </linearGradient>
          <linearGradient id="cityAsphalt" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1C1917" />
            <stop offset="100%" stopColor="#090503" />
          </linearGradient>
        </defs>

        {/* Fondo del cielo saturado de resplandor anaranjado, cielo ciego sin estrellas */}
        <rect width="1920" height="1080" fill="url(#skyglowDome)" opacity={pulseSky} />

        {/* Haces de luz descontrolados disparados hacia el cielo (reflectores de eventos y centros comerciales) */}
        <polygon points={`380,780 ${440 + beamShift},60 ${490 + beamShift},60 410,780`} fill="url(#beamGradient)" />
        <polygon points={`1420,780 ${1360 - beamShift},40 ${1410 - beamShift},40 1450,780`} fill="url(#beamGradient)" />

        {/* Capa de rascacielos al fondo (siluetas oscuras recortadas contra el resplandor artificial) */}
        {[
          { x: 80, w: 140, h: 480 },
          { x: 260, w: 160, h: 560 },
          { x: 460, w: 120, h: 410 },
          { x: 620, w: 180, h: 510 },
          { x: 1120, w: 170, h: 590 },
          { x: 1330, w: 130, h: 460 },
          { x: 1500, w: 190, h: 540 },
          { x: 1730, w: 130, h: 430 },
        ].map((b, idx) => (
          <g key={`skysc-${idx}`}>
            <rect
              x={b.x}
              y={780 - b.h}
              width={b.w}
              height={b.h}
              fill="#1F130B"
              stroke="#000000"
              strokeWidth="5"
            />
            {/* Ventanas iluminadas en amarillo caótico */}
            {[...Array(6)].map((_, r) => (
              <line
                key={`win-${idx}-${r}`}
                x1={b.x + 18}
                y1={780 - b.h + 50 + r * 65}
                x2={b.x + b.w - 18}
                y2={780 - b.h + 50 + r * 65}
                stroke="#FEF08A"
                strokeWidth="4"
                strokeDasharray="14 12"
                opacity="0.8"
              />
            ))}
            <circle cx={b.x + b.w / 2} cy={780 - b.h - 8} r="5" fill="#EF4444" />
          </g>
        ))}

        {/* Farolas de alumbrado público con globos difusores no apantallados (emiten luz a 360 grados) */}
        {[320, 840, 1620].map((lx, idx) => (
          <g key={`lamp-${idx}`}>
            <line x1={lx} y1={780} x2={lx} y2={620} stroke="#44403C" strokeWidth="8" strokeLinecap="round" />
            <path d={`M ${lx - 25} 620 L ${lx + 25} 620 L ${lx} 590 Z`} fill="#1C1917" stroke="#000" strokeWidth="3" />
            {/* Foco globo incandescente/mercurio irradiando halo esférico de luz contaminante */}
            <circle cx={lx} cy={605} r="28" fill="#FDE047" opacity="0.3" />
            <circle cx={lx} cy={605} r="16" fill="#FEF08A" opacity="0.65" />
            <circle cx={lx} cy={605} r="9" fill="#FFFFFF" stroke="#F59E0B" strokeWidth="2.5" />
          </g>
        ))}

        {/* Suelo urbano en primer plano con bordillo y asfalto */}
        <rect x="0" y="780" width="1920" height="300" fill="url(#cityAsphalt)" stroke="#78350F" strokeWidth="7" />
        <line x1="0" y1="786" x2="1920" y2="786" stroke="#F59E0B" strokeWidth="3" strokeDasharray="30 20" opacity="0.5" />
      </svg>
    </div>
  );
};

/** 15. Observatorio Astronómico en Cumbre de Alta Montaña */
const ObservatorioAstronomicoCumbreStage: React.FC<{ frame: number }> = ({ frame }) => {
  const domeTwinkle = 0.6 + Math.sin(frame * 0.15) * 0.35;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#020617] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="nightSkyDeep" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#020617" />
            <stop offset="60%" stopColor="#0B132B" />
            <stop offset="100%" stopColor="#1E293B" />
          </linearGradient>
          <linearGradient id="mountainRidge" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E293B" />
            <stop offset="100%" stopColor="#0A0F1D" />
          </linearGradient>
        </defs>

        <rect width="1920" height="1080" fill="url(#nightSkyDeep)" />

        {/* Campo estelar nítido en gran altitud */}
        {[
          [120, 110, 2.5], [240, 70, 1.8], [390, 140, 2.2], [540, 90, 1.5], [720, 160, 2.8],
          [880, 80, 2.0], [1050, 130, 2.4], [1210, 60, 1.6], [1390, 110, 2.6], [1560, 75, 1.9],
          [1720, 135, 2.2], [1840, 95, 1.7], [310, 210, 2.0], [840, 230, 1.5], [1480, 220, 2.4]
        ].map(([sx, sy, sr], idx) => (
          <circle
            key={`st-${idx}`}
            cx={sx}
            cy={sy}
            r={sr}
            fill="#E0F2FE"
            opacity={(0.5 + Math.sin(frame * 0.12 + idx) * 0.45).toFixed(2)}
          />
        ))}

        {/* Siluetas de cordilleras montañosas lejanas */}
        <polygon points="0,680 280,510 580,620 920,470 1280,580 1620,490 1920,640 1920,780 0,780" fill="url(#mountainRidge)" stroke="#0F172A" strokeWidth="4" />

        {/* Cúpula clásica de observatorio astronómico a la izquierda */}
        <g transform="translate(240, 480)">
          {/* Base cilíndrica */}
          <rect x="-80" y="80" width="160" height="120" fill="#CBD5E1" stroke="#000000" strokeWidth="6" />
          {/* Cúpula semiesférica */}
          <path d="M -90 80 A 90 90 0 0 1 90 80 Z" fill="#E2E8F0" stroke="#000000" strokeWidth="7" />
          {/* Ranura de observación abierta con interior oscuro y telescopio asomando */}
          <rect x="-24" y="-8" width="48" height="92" fill="#020617" stroke="#38BDF8" strokeWidth="4" />
          <line x1="-12" y1="20" x2="28" y2="-15" stroke="#FFE600" strokeWidth="7" strokeLinecap="round" />
          <circle cx="0" cy="80" r="8" fill="#EF4444" opacity={domeTwinkle} />
        </g>

        {/* Cúpula moderna menor y antena parabólica a la derecha */}
        <g transform="translate(1640, 520)">
          <rect x="-60" y="70" width="120" height="90" fill="#94A3B8" stroke="#000" strokeWidth="5" />
          <path d="M -70 70 A 70 70 0 0 1 70 70 Z" fill="#CBD5E1" stroke="#000" strokeWidth="6" />
          <line x1="80" y1="160" x2="80" y2="40" stroke="#64748B" strokeWidth="5" />
          <path d="M 60 50 Q 80 30 100 50" fill="none" stroke="#38BDF8" strokeWidth="4" />
        </g>

        {/* Explanada rocosa de la cumbre en primer plano */}
        <rect x="0" y="780" width="1920" height="300" fill="#0F172A" stroke="#38BDF8" strokeWidth="6" />
        <line x1="0" y1="792" x2="1920" y2="792" stroke="#334155" strokeWidth="4" strokeDasharray="16 12" />
      </svg>
    </div>
  );
};

/** 16. Playa Costera Nocturna (Mar vs Resplandor Urbano Hotelero) */
const PlayaCostaNocturnaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const waveShift = Math.sin(frame * 0.18) * 18;
  const hotelGlow = 0.75 + Math.sin(frame * 0.13) * 0.2;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#06121E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="beachSky" x1="0" y1="0" x2="1" y2="0">
            {/* Lado izquierdo oscuro oceánico -> Lado derecho contaminado por hoteles */}
            <stop offset="0%" stopColor="#030A14" />
            <stop offset="55%" stopColor="#082F49" />
            <stop offset="100%" stopColor="#B45309" />
          </linearGradient>
          <linearGradient id="seaWater" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#082F49" />
            <stop offset="100%" stopColor="#0284C7" />
          </linearGradient>
          <linearGradient id="sandGround" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#D97706" />
            <stop offset="100%" stopColor="#78350F" />
          </linearGradient>
        </defs>

        <rect width="1920" height="1080" fill="url(#beachSky)" />

        {/* Luna creciente pálida a la izquierda sobre el mar */}
        <g transform="translate(260, 160)">
          <circle cx="0" cy="0" r="38" fill="#FEF08A" stroke="#000" strokeWidth="4" />
          <circle cx="16" cy="-6" r="32" fill="#030A14" />
        </g>

        {/* Resplandor cegador de complejos hoteleros en la costa derecha */}
        <g opacity={hotelGlow}>
          <polygon points="1280,780 1380,480 1520,480 1620,780" fill="#F59E0B" opacity="0.3" />
          <rect x="1420" y="520" width="130" height="260" fill="#1C1917" stroke="#000" strokeWidth="5" />
          <rect x="1570" y="440" width="170" height="340" fill="#1E293B" stroke="#000" strokeWidth="6" />
          {/* Rótulo luminoso de hotel */}
          <rect x="1440" y="540" width="90" height="24" rx="4" fill="#EF4444" />
          <text x="1485" y="556" textAnchor="middle" fontSize="12" fontWeight="900" fill="#FFFFFF">RESORT</text>
          {/* Focos y reflectores dirigidos a la playa */}
          <line x1="1485" y1="780" x2="1140" y2="780" stroke="#FDE047" strokeWidth="4" opacity="0.6" strokeDasharray="16 10" />
        </g>

        {/* Océano con olas rompiendo a la izquierda */}
        <path
          d={`M 0 680 Q ${320 + waveShift} 660 640 710 Q 820 740 980 780 L 0 780 Z`}
          fill="url(#seaWater)"
          stroke="#38BDF8"
          strokeWidth="6"
        />
        {/* Espuma marina plateada */}
        <path
          d={`M 0 690 Q ${310 + waveShift} 670 630 718 L 0 718 Z`}
          fill="#E0F2FE"
          opacity="0.75"
        />

        {/* Arena de la playa en primer plano con huellas de tortuga */}
        <rect x="0" y="780" width="1920" height="300" fill="url(#sandGround)" stroke="#451A03" strokeWidth="8" />
        {/* Rastro ondulante de aletas de tortuga marina en la arena */}
        <path d="M 420 860 Q 640 830 890 855 T 1320 840" fill="none" stroke="#78350F" strokeWidth="8" strokeDasharray="14 16" />
      </svg>
    </div>
  );
};

/** 17. Maqueta Urbana de Control e Interruptores Eléctricos */
const MaquetaUrbanaInterruptoresStage: React.FC<{ frame: number }> = ({ frame }) => {
  const gridPulse = 0.8 + Math.sin(frame * 0.16) * 0.18;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B0F19] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <pattern id="cadGrid" width="60" height="60" patternUnits="userSpaceOnUse">
            <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#1E293B" strokeWidth="1.5" opacity="0.6" />
          </pattern>
        </defs>

        {/* Fondo de sala de comando de ingeniería y esquemas técnicos */}
        <rect width="1920" height="1080" fill="#0B0F19" />
        <rect width="1920" height="780" fill="url(#cadGrid)" />

        {/* Esquemas murales de red eléctrica de distribución */}
        <g opacity="0.65" transform="translate(180, 120)">
          <rect x="0" y="0" width="340" height="220" rx="10" fill="#0F172A" stroke="#0284C7" strokeWidth="4" />
          <text x="20" y="36" fontSize="16" fontWeight="900" fill="#38BDF8">CIRCUITO URBANO 16X9</text>
          <line x1="20" y1="80" x2="300" y2="80" stroke="#FFE600" strokeWidth="4" />
          <line x1="120" y1="80" x2="120" y2="180" stroke="#FFE600" strokeWidth="3" />
          <circle cx="120" cy="180" r="14" fill="#EF4444" />
          <text x="145" y="185" fontSize="13" fontWeight="900" fill="#EF4444">SUBESTACIÓN 220 KV</text>
        </g>

        {/* Mesa de maqueta arquitectónica 3D iluminada al centro */}
        <g transform="translate(680, 430)">
          {/* Base de la maqueta isométrica */}
          <polygon points="280,-40 680,70 280,240 -120,130" fill="#1E293B" stroke="#38BDF8" strokeWidth="5" />
          {/* Bloques de edificios miniatura en la maqueta */}
          {[
            { x: 140, y: 30, w: 50, h: 110, c: "#FDE047" },
            { x: 220, y: 10, w: 65, h: 160, c: "#EF4444" },
            { x: 320, y: 50, w: 55, h: 90, c: "#FDE047" },
            { x: 410, y: 30, w: 70, h: 140, c: "#38BDF8" },
          ].map((m, idx) => (
            <g key={`maq-${idx}`}>
              <rect x={m.x} y={m.y - m.h} width={m.w} height={m.h} fill="#0F172A" stroke="#000" strokeWidth="3" />
              <circle cx={m.x + m.w / 2} cy={m.y - m.h - 8} r="5" fill={m.c} opacity={gridPulse} />
            </g>
          ))}
          {/* Calles iluminadas de la maqueta */}
          <line x1="110" y1="80" x2="490" y2="80" stroke="#FFE600" strokeWidth="4" strokeDasharray="8 6" />
        </g>

        {/* Consola industrial de interruptores de cuchilla y barrajes en primer plano */}
        <rect x="0" y="780" width="1920" height="300" fill="#0F172A" stroke="#FFE600" strokeWidth="7" />
        <rect x="180" y="805" width="460" height="110" rx="8" fill="#1E293B" stroke="#334155" strokeWidth="4" />
        <text x="210" y="845" fontSize="20" fontWeight="900" fill="#FFE600">INTERRUPTOR MAESTRO GRID-A</text>
        <line x1="210" y1="875" x2="600" y2="875" stroke="#22C55E" strokeWidth="8" strokeLinecap="round" />
      </svg>
    </div>
  );
};

/** 18. Santuario de Cielo Estrellado Clase 1 de la Escala Bortle (Vía Láctea Majestuosa) */
const SantuarioCieloEstrelladoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const cosmicPulse = 0.88 + Math.sin(frame * 0.12) * 0.12;
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#02040A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          {/* Arco cósmico de la Vía Láctea con polvo interestelar y cúmulos brillantes */}
          <linearGradient id="milkyWayCore" x1="0" y1="1" x2="1" y2="0">
            <stop offset="0%" stopColor="#0B132B" stopOpacity="0.2" />
            <stop offset="30%" stopColor="#4338CA" stopOpacity="0.65" />
            <stop offset="50%" stopColor="#A855F7" stopOpacity="0.75" />
            <stop offset="65%" stopColor="#38BDF8" stopOpacity="0.6" />
            <stop offset="100%" stopColor="#0B132B" stopOpacity="0.2" />
          </linearGradient>
          <linearGradient id="airglowGreen" x1="0" y1="1" x2="0" y2="0">
            <stop offset="0%" stopColor="#10B981" stopOpacity="0.28" />
            <stop offset="40%" stopColor="#059669" stopOpacity="0.12" />
            <stop offset="100%" stopColor="#02040A" stopOpacity="0" />
          </linearGradient>
          <linearGradient id="desertPlateau" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E1B4B" />
            <stop offset="100%" stopColor="#090514" />
          </linearGradient>
        </defs>

        <rect width="1920" height="1080" fill="#02040A" />

        {/* Resplandor atmosférico natural (Airglow verde sutil sobre el horizonte) */}
        <rect x="0" y="440" width="1920" height="340" fill="url(#airglowGreen)" />

        {/* Banda diagonal majestuosa de la Vía Láctea atravesando el firmamento */}
        <g opacity={cosmicPulse}>
          <ellipse cx="980" cy="340" rx="940" ry="210" transform="rotate(-28 980 340)" fill="url(#milkyWayCore)" />
          {/* Nubes oscuras de polvo interestelar (Gran Grieta de la Vía Láctea) */}
          <path
            d="M 520 540 Q 760 380 980 320 Q 1240 260 1480 180 Q 1260 290 1020 370 Q 780 440 520 540 Z"
            fill="#02040A"
            opacity="0.85"
          />
        </g>

        {/* Miles de estrellas nítidas de clase Bortle 1 */}
        {[
          [140, 80, 2.8, "#FFE600"], [280, 160, 1.8, "#FFFFFF"], [420, 60, 2.2, "#38BDF8"],
          [580, 220, 3.2, "#FFFFFF"], [690, 110, 1.6, "#FBCFE8"], [810, 180, 2.4, "#FFFFFF"],
          [940, 70, 3.6, "#FEF08A"], [1070, 150, 2.0, "#38BDF8"], [1190, 95, 2.8, "#FFFFFF"],
          [1340, 240, 1.7, "#FFFFFF"], [1460, 130, 3.0, "#A7F3D0"], [1610, 80, 2.2, "#FFFFFF"],
          [1740, 190, 2.6, "#FFFFFF"], [1860, 110, 1.8, "#FEF08A"], [320, 320, 2.4, "#FFFFFF"],
          [740, 390, 2.0, "#38BDF8"], [1280, 360, 2.5, "#FFFFFF"], [1590, 330, 2.1, "#FFFFFF"]
        ].map(([sx, sy, sr, sc], idx) => (
          <circle
            key={`bortle-st-${idx}`}
            cx={sx as number}
            cy={sy as number}
            r={sr as number}
            fill={sc as string}
            opacity={(0.6 + Math.sin(frame * 0.14 + idx * 0.8) * 0.4).toFixed(2)}
          />
        ))}

        {/* Siluetas de mesetas y volcanes lejanos del desierto de Atacama / La Palma */}
        <polygon points="0,710 340,620 620,680 960,580 1340,660 1680,610 1920,690 1920,780 0,780" fill="#0A0818" stroke="#000" strokeWidth="4" />

        {/* Silueta de telescopio de aficionado sobre trípode en la cresta */}
        <g transform="translate(1420, 640)">
          <line x1="0" y1="40" x2="-22" y2="140" stroke="#000" strokeWidth="6" />
          <line x1="0" y1="40" x2="22" y2="140" stroke="#000" strokeWidth="6" />
          <line x1="0" y1="40" x2="0" y2="140" stroke="#000" strokeWidth="6" />
          <rect x="-34" y="24" width="78" height="20" rx="4" transform="rotate(-32 5 34)" fill="#38BDF8" stroke="#000" strokeWidth="4" />
        </g>

        {/* Meseta rocosa desértica en primer plano */}
        <rect x="0" y="780" width="1920" height="300" fill="url(#desertPlateau)" stroke="#38BDF8" strokeWidth="7" />
        <line x1="0" y1="794" x2="1920" y2="794" stroke="#6366F1" strokeWidth="4" strokeDasharray="24 16" />
      </svg>
    </div>
  );
};

/** Salón Comedor Familiar estilo "The Last Supper" con banquete, lámparas cálidas y retratos */
const ComedorFamiliarStage: React.FC<{ frame: number }> = ({ frame }) => {
  const steamOsc1 = Math.sin(frame * 0.12) * 8;
  const steamOsc2 = Math.cos(frame * 0.15) * 8;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#2D1B16] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          {/* Fondo degradado cálido de pared */}
          <linearGradient id="diningWall" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#3F231D" />
            <stop offset="65%" stopColor="#5A342B" />
            <stop offset="100%" stopColor="#2A1410" />
          </linearGradient>

          {/* Luz cálida de lámparas superiores */}
          <radialGradient id="lampCone" cx="50%" cy="0%" r="90%">
            <stop offset="0%" stopColor="#FEF08A" stopOpacity="0.4" />
            <stop offset="50%" stopColor="#F59E0B" stopOpacity="0.15" />
            <stop offset="100%" stopColor="#2A1410" stopOpacity="0" />
          </radialGradient>

          {/* Ventana con cielo atardecer */}
          <linearGradient id="windowSunset" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#4338CA" />
            <stop offset="50%" stopColor="#BE185D" />
            <stop offset="100%" stopColor="#F97316" />
          </linearGradient>
        </defs>

        {/* Pared con papel tapiz cálido */}
        <rect width="1920" height="820" fill="url(#diningWall)" />

        {/* Patrón sutil de puntos de papel tapiz */}
        {Array.from({ length: 48 }).map((_, idx) => {
          const px = (idx % 12) * 160 + 80;
          const py = Math.floor(idx / 12) * 130 + 80;
          return (
            <circle
              key={`dot-${idx}`}
              cx={px}
              cy={py}
              r="4"
              fill="#FDE68A"
              opacity="0.12"
            />
          );
        })}

        {/* Ventana derecha con atardecer */}
        <g transform="translate(1360, 140)">
          <rect x="-8" y="-8" width="376" height="396" rx="8" fill="#FFFFFF" stroke="#000000" strokeWidth="6" />
          <rect width="360" height="380" rx="4" fill="url(#windowSunset)" />
          {/* Cortinas laterales */}
          <path d="M 0 0 Q 60 180 30 380 L 0 380 Z" fill="#0D9488" stroke="#000000" strokeWidth="4" />
          <path d="M 360 0 Q 300 180 330 380 L 360 380 Z" fill="#0D9488" stroke="#000000" strokeWidth="4" />
          {/* Marcos de ventana */}
          <line x1="180" y1="0" x2="180" y2="380" stroke="#FFFFFF" strokeWidth="8" />
          <line x1="0" y1="190" x2="360" y2="190" stroke="#FFFFFF" strokeWidth="8" />
        </g>

        {/* Cuadros de retratos familiares en la pared izquierda */}
        <g transform="translate(200, 180)">
          <rect x="0" y="0" width="150" height="180" rx="6" fill="#F8FAFC" stroke="#000000" strokeWidth="6" />
          <circle cx="75" cy="70" r="28" fill="#1E293B" />
          <circle cx="75" cy="130" r="34" fill="#1E293B" />
        </g>
        <g transform="translate(400, 220)">
          <rect x="0" y="0" width="120" height="140" rx="6" fill="#F8FAFC" stroke="#000000" strokeWidth="6" />
          <circle cx="60" cy="55" r="20" fill="#1E293B" />
          <circle cx="60" cy="100" r="26" fill="#1E293B" />
        </g>
        <g transform="translate(560, 170)">
          <rect x="0" y="0" width="110" height="130" rx="6" fill="#F8FAFC" stroke="#000000" strokeWidth="6" />
          <circle cx="55" cy="50" r="18" fill="#1E293B" />
          <circle cx="55" cy="90" r="24" fill="#1E293B" />
        </g>

        {/* Conos de luz cálida colgantes desde el techo */}
        <polygon points="460,0 280,720 640,720" fill="url(#lampCone)" />
        <polygon points="960,0 760,720 1160,720" fill="url(#lampCone)" />
        <polygon points="1460,0 1280,720 1640,720" fill="url(#lampCone)" />

        {/* Lámparas / candelabros colgantes */}
        {[460, 960, 1460].map((lx) => (
          <g key={`lamp-${lx}`} transform={`translate(${lx}, 0)`}>
            <line x1="0" y1="0" x2="0" y2="70" stroke="#000000" strokeWidth="4" />
            <ellipse cx="0" cy="74" rx="28" ry="10" fill="#FACC15" stroke="#000000" strokeWidth="4" />
            <circle cx="0" cy="80" r="14" fill="#FEF08A" />
          </g>
        ))}

        {/* Respaldos de sillas de madera detrás de los comensales */}
        {[300, 520, 740, 960, 1180, 1400, 1620].map((cx) => (
          <g key={`chair-${cx}`} transform={`translate(${cx}, 380)`}>
            <rect x="-42" y="0" width="84" height="250" rx="14" fill="#451A03" stroke="#000000" strokeWidth="5" />
            <rect x="-32" y="14" width="64" height="60" rx="8" fill="#5A280B" />
          </g>
        ))}

        {/* Suelo de madera noble */}
        <rect x="0" y="820" width="1920" height="260" fill="#1C0E0B" stroke="#000000" strokeWidth="6" />
        <line x1="0" y1="890" x2="1920" y2="890" stroke="#2A1410" strokeWidth="3" />
        <line x1="0" y1="970" x2="1920" y2="970" stroke="#2A1410" strokeWidth="3" />
      </svg>
    </div>
  );
};

/** Capa de primer plano para la Mesa de Banquete (se renderiza por delante de los personajes sentados) */
export const MesaComedorFamiliarForeground: React.FC<{ frame: number }> = ({ frame }) => {
  const steamOsc1 = Math.sin(frame * 0.12) * 8;
  const steamOsc2 = Math.cos(frame * 0.15) * 8;

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden" style={{ zIndex: 25 }}>
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Gran Mesa de Banquete corrida con mantel blanco largo que cubre las piernas */}
        <g transform="translate(60, 600)">
          {/* Sombra proyectada bajo el mantel */}
          <rect x="0" y="240" width="1800" height="40" fill="#0A0504" opacity="0.6" />
          {/* Faldón del mantel blanco brillante */}
          <rect x="0" y="0" width="1800" height="240" rx="12" fill="#FFFFFF" stroke="#000000" strokeWidth="6" />
          {/* Pliegues verticales elegantes del mantel */}
          {Array.from({ length: 22 }).map((_, i) => (
            <line
              key={`crease-${i}`}
              x1={i * 82 + 40}
              y1="40"
              x2={i * 82 + 40}
              y2="236"
              stroke="#E2E8F0"
              strokeWidth="4"
              strokeLinecap="round"
            />
          ))}

          {/* Bandeja con banquete central y vapor ascendente */}
          <g transform="translate(900, -28)">
            <ellipse cx="0" cy="24" rx="100" ry="24" fill="#E2E8F0" stroke="#000000" strokeWidth="5" />
            <ellipse cx="0" cy="14" rx="75" ry="32" fill="#D97706" stroke="#000000" strokeWidth="5" />
            {/* Vapor animado */}
            <path
              d={`M -20 -10 Q ${-30 + steamOsc1} -50 -10 -90`}
              fill="none"
              stroke="#FEF3C7"
              strokeWidth="4"
              strokeLinecap="round"
              opacity="0.65"
            />
            <path
              d={`M 20 -10 Q ${30 + steamOsc2} -50 10 -90`}
              fill="none"
              stroke="#FEF3C7"
              strokeWidth="4"
              strokeLinecap="round"
              opacity="0.65"
            />
          </g>

          {/* Platos en cada posición */}
          {[180, 400, 620, 840, 1060, 1280, 1500].map((px) => (
            <ellipse
              key={`plate-${px}`}
              cx={px}
              cy="2"
              rx="48"
              ry="12"
              fill="#F8FAFC"
              stroke="#000000"
              strokeWidth="4"
            />
          ))}
        </g>
      </svg>
    </div>
  );
};

/** Calle Europea / Corner Café (fachada de café, toldo a rayas, farola vintage y buzón) */
const CalleCafeCornerStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="skyTwilight" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#1E1B4B" />
            <stop offset="60%" stopColor="#312E81" />
            <stop offset="100%" stopColor="#F59E0B" stopOpacity="0.4" />
          </linearGradient>
          <radialGradient id="streetLampCone" cx="50%" cy="0%" r="90%">
            <stop offset="0%" stopColor="#FEF08A" stopOpacity="0.45" />
            <stop offset="60%" stopColor="#FBBF24" stopOpacity="0.15" />
            <stop offset="100%" stopColor="#0F172A" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Cielo crepuscular */}
        <rect width="1920" height="760" fill="url(#skyTwilight)" />

        {/* Fachada del edificio café */}
        <rect x="220" y="160" width="1080" height="600" fill="#1E3A2F" stroke="#000000" strokeWidth="6" />

        {/* Ventanales grandes con luz interior cálida */}
        <rect x="260" y="320" width="600" height="420" rx="6" fill="#FEF3C7" stroke="#000000" strokeWidth="6" />
        <line x1="560" y1="320" x2="560" y2="740" stroke="#1E3A2F" strokeWidth="10" />

        {/* Letrero "CORNER CAFÉ" */}
        <rect x="360" y="200" width="580" height="90" rx="8" fill="#142B23" stroke="#000000" strokeWidth="6" />
        <text
          x="650"
          y="262"
          textAnchor="middle"
          fill="#FFFFFF"
          fontSize="48"
          fontWeight="900"
          fontFamily="system-ui, sans-serif"
          letterSpacing="4"
        >
          CORNER CAFÉ
        </text>

        {/* Toldo a rayas rojas y blancas */}
        <g transform="translate(240, 280)">
          {Array.from({ length: 16 }).map((_, i) => (
            <polygon
              key={`stripe-${i}`}
              points={`${i * 42},0 ${i * 42 + 42},0 ${i * 42 + 36},65 ${i * 42 - 6},65`}
              fill={i % 2 === 0 ? "#DC2626" : "#FFFFFF"}
              stroke="#000000"
              strokeWidth="4"
            />
          ))}
        </g>

        {/* Puerta del café con cartel OPEN */}
        <rect x="900" y="380" width="180" height="360" rx="6" fill="#0F241C" stroke="#000000" strokeWidth="6" />
        <rect x="940" y="440" width="100" height="50" rx="6" fill="#EC4899" stroke="#000000" strokeWidth="4" />
        <text x="990" y="475" textAnchor="middle" fill="#FFFFFF" fontSize="20" fontWeight="bold">
          OPEN
        </text>

        {/* Edificio de la derecha (persiana metálica cerrada) */}
        <rect x="1340" y="240" width="540" height="520" fill="#334155" stroke="#000000" strokeWidth="6" />
        <rect x="1380" y="340" width="440" height="420" fill="#475569" stroke="#000000" strokeWidth="6" />
        {Array.from({ length: 12 }).map((_, i) => (
          <line
            key={`shutter-${i}`}
            x1="1380"
            y1={360 + i * 32}
            x2="1820"
            y2={360 + i * 32}
            stroke="#1E293B"
            strokeWidth="3"
          />
        ))}

        {/* Acera / pavimento peatonal */}
        <rect x="0" y="760" width="1920" height="140" fill="#CBD5E1" stroke="#000000" strokeWidth="6" />
        <line x1="0" y1="840" x2="1920" y2="840" stroke="#94A3B8" strokeWidth="3" strokeDasharray="30 20" />

        {/* Calzada / asfalto */}
        <rect x="0" y="900" width="1920" height="180" fill="#1E293B" stroke="#000000" strokeWidth="6" />

        {/* Buzón rojo británico vintage */}
        <g transform="translate(1420, 680)">
          <path d="M 0 40 C 0 -10 60 -10 60 40 L 60 140 L 0 140 Z" fill="#DC2626" stroke="#000000" strokeWidth="5" />
          <rect x="12" y="34" width="36" height="6" rx="2" fill="#000000" />
          <rect x="16" y="55" width="28" height="24" rx="2" fill="#FFFFFF" />
        </g>

        {/* Farola vintage con cono de luz */}
        <g transform="translate(1260, 220)">
          <polygon points="30,0 -180,620 240,620" fill="url(#streetLampCone)" />
          {/* Poste */}
          <line x1="30" y1="0" x2="30" y2="540" stroke="#0F172A" strokeWidth="12" />
          <path d="M 30 0 Q 0 -40 -30 -20" fill="none" stroke="#0F172A" strokeWidth="10" strokeLinecap="round" />
          <polygon points="-44,-20 -16,-20 -20,20 -40,20" fill="#FEF08A" stroke="#0F172A" strokeWidth="4" />
        </g>

        {/* Mesa bistro exterior con croissant y taza */}
        <g transform="translate(420, 710)">
          <line x1="0" y1="20" x2="0" y2="100" stroke="#000000" strokeWidth="6" />
          <ellipse cx="0" cy="20" rx="55" ry="14" fill="#FFFFFF" stroke="#000000" strokeWidth="5" />
          {/* Taza de café */}
          <rect x="16" y="2" width="18" height="14" rx="3" fill="#FFFFFF" stroke="#000000" strokeWidth="3" />
          {/* Croissant dorado */}
          <ellipse cx="-16" cy="10" rx="16" ry="8" fill="#F59E0B" stroke="#000000" strokeWidth="2.5" />
        </g>

        {/* Macetero decorativo con planta */}
        <g transform="translate(760, 690)">
          <polygon points="0,50 60,50 50,110 10,110" fill="#B45309" stroke="#000000" strokeWidth="5" />
          <ellipse cx="30" cy="40" rx="42" ry="24" fill="#15803D" stroke="#000000" strokeWidth="4" />
        </g>
      </svg>
    </div>
  );
};

/**
 * Escenario 1: Despacho Histórico de Albert Einstein (Berlín / Academia Prusiana, 1915).
 * Estudio con pizarra llena de ecuaciones tensoriales, ventanal a cielo estrellado,
 * biblioteca victoriana de nogal y lámpara de latón.
 */
export const DespachoEinsteinStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pendulumAngle = Math.sin(frame * 0.12) * 12;
  const lampGlow = 0.88 + Math.sin(frame * 0.16) * 0.08;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1A1009] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="einsteinWallGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#2E1C11" />
            <stop offset="65%" stopColor="#1C1009" />
            <stop offset="100%" stopColor="#0F0804" />
          </linearGradient>
          <linearGradient id="einsteinFloorGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#3E2718" />
            <stop offset="100%" stopColor="#1F120A" />
          </linearGradient>
          <radialGradient id="deskLampCone" cx="0.5" cy="0.1" r="0.8">
            <stop offset="0%" stopColor="#FEF3C7" stopOpacity={0.45 * lampGlow} />
            <stop offset="45%" stopColor="#F59E0B" stopOpacity={0.18 * lampGlow} />
            <stop offset="100%" stopColor="#1A1009" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* 1. Fondo de pared de roble y papel tapiz victoriano oscuro */}
        <rect x="0" y="0" width="1920" height="740" fill="url(#einsteinWallGrad)" />

        {/* Zócalo y molduras de madera tallada */}
        <rect x="0" y="690" width="1920" height="50" fill="#170C05" stroke="#000000" strokeWidth="4" />
        <line x1="0" y1="710" x2="1920" y2="710" stroke="#3D2110" strokeWidth="3" />

        {/* 2. Suelo de parquet con perspectiva neo-brutalista */}
        <polygon points="0,740 1920,740 1920,1080 0,1080" fill="url(#einsteinFloorGrad)" stroke="#000000" strokeWidth="6" />
        {[-4, -3, -2, -1, 0, 1, 2, 3, 4].map((i) => (
          <line
            key={`parquet-${i}`}
            x1={960 + i * 160}
            y1="740"
            x2={960 + i * 320}
            y2="1080"
            stroke="#170C05"
            strokeWidth="3.5"
          />
        ))}

        {/* 3. Gran ventanal ojival hacia la noche de Berlín 1915 (Lado izquierdo) */}
        <g transform="translate(140, 120)">
          {/* Marco exterior */}
          <rect x="-10" y="-10" width="340" height="520" rx="20" fill="#0A0503" stroke="#000000" strokeWidth="6" />
          {/* Cielo estrellado detrás del vidrio */}
          <rect x="0" y="0" width="320" height="500" rx="14" fill="#030712" />
          {/* Estrellas lejanas */}
          {Array.from({ length: 30 }).map((_, i) => (
            <circle
              key={`star-${i}`}
              cx={(i * 37) % 300 + 10}
              cy={(i * 53) % 460 + 15}
              r={(i % 3) * 0.8 + 1.2}
              fill="#F8FAFC"
              opacity={0.6 + Math.sin(frame * 0.15 + i) * 0.4}
            />
          ))}
          {/* Silueta lejana de cúpulas de Berlín */}
          <path d="M 0 460 Q 60 410 120 460 L 160 430 L 220 460 L 320 440 L 320 500 L 0 500 Z" fill="#020617" />
          {/* Parteluces de madera del ventanal */}
          <line x1="160" y1="0" x2="160" y2="500" stroke="#1A1009" strokeWidth="8" />
          <line x1="0" y1="220" x2="320" y2="220" stroke="#1A1009" strokeWidth="8" />
          <line x1="0" y1="360" x2="320" y2="360" stroke="#1A1009" strokeWidth="6" />
        </g>

        {/* 4. Gran Pizarra Académica en el centro con las Ecuaciones de Campo de Einstein */}
        <g transform="translate(580, 130)">
          {/* Marco de madera de la pizarra con sombra dura */}
          <rect x="8" y="8" width="860" height="480" rx="8" fill="#000000" opacity="0.6" />
          <rect x="0" y="0" width="860" height="480" rx="8" fill="#1C1917" stroke="#3D2110" strokeWidth="12" />
          {/* Superficie pizarra verde pizarra oscuro */}
          <rect x="14" y="14" width="832" height="452" rx="4" fill="#06281B" stroke="#000000" strokeWidth="4" />

          {/* Rótulo superior en tiza */}
          <text x="430" y="65" textAnchor="middle" fill="#FEF08A" fontSize="24" fontWeight="900" fontFamily="'Courier New', monospace" letterSpacing="2">
            ACADEMIA PRUSIANA DE CIENCIAS — NOVIEMBRE 1915
          </text>
          <line x1="120" y1="80" x2="740" y2="80" stroke="#4ADE80" strokeWidth="2.5" strokeDasharray="8 6" opacity="0.7" />

          {/* Ecuación central de Campo de Einstein */}
          <text x="430" y="150" textAnchor="middle" fill="#FFFFFF" fontSize="36" fontWeight="900" fontFamily="'Times New Roman', serif" letterSpacing="1">
            G_μν = 8π G / c⁴ · T_μν
          </text>
          <text x="430" y="188" textAnchor="middle" fill="#93C5FD" fontSize="20" fontWeight="700" fontFamily="'Courier New', monospace">
            R_μν - 1/2 · g_μν · R = κ · T_μν
          </text>

          {/* Solución de Schwarzschild (Diciembre 1915) */}
          <rect x="60" y="225" width="712" height="110" rx="6" fill="#031F14" stroke="#22C55E" strokeWidth="2.5" strokeDasharray="6 4" />
          <text x="80" y="260" fill="#38BDF8" fontSize="18" fontWeight="bold" fontFamily="'Courier New', monospace">
            MÉTRICA DE SCHWARZSCHILD (DESDE EL FRENTE RUSO):
          </text>
          <text x="80" y="295" fill="#FEF9C3" fontSize="22" fontWeight="900" fontFamily="'Times New Roman', serif">
            ds² = -(1 - 2GM/c²r) c²dt² + (1 - 2GM/c²r)⁻¹ dr² + r²dΩ²
          </text>
          <text x="80" y="325" fill="#F87171" fontSize="17" fontWeight="bold" fontFamily="'Courier New', monospace">
            SI r = 2GM/c² → (1 - 2GM/c²r) = 0 → ¡DENOMINADOR COLAPSA A CERO!
          </text>

          {/* Diagrama de cono de luz y curvatura dibujado en tiza */}
          <g transform="translate(620, 360)">
            <ellipse cx="60" cy="40" rx="55" ry="16" fill="none" stroke="#FDE047" strokeWidth="2" strokeDasharray="4 3" />
            <line x1="5" y1="40" x2="60" y2="85" stroke="#FDE047" strokeWidth="2" />
            <line x1="115" y1="40" x2="60" y2="85" stroke="#FDE047" strokeWidth="2" />
            <text x="60" y="102" textAnchor="middle" fill="#FDE047" fontSize="13" fontWeight="bold" fontFamily="'Courier New', monospace">
              CONO DE LUZ
            </text>
          </g>

          {/* Bandeja de tizas y borrador inferior */}
          <rect x="200" y="460" width="460" height="14" rx="2" fill="#78350F" stroke="#000000" strokeWidth="3" />
          <rect x="230" y="454" width="60" height="8" rx="2" fill="#E2E8F0" />
          <rect x="310" y="454" width="70" height="9" rx="2" fill="#FDE047" />
          <rect x="420" y="450" width="80" height="12" rx="3" fill="#374151" stroke="#000000" strokeWidth="2" />
        </g>

        {/* 5. Gran Librería clásica de pared completa (Lado derecho) */}
        <g transform="translate(1520, 110)">
          <rect x="0" y="0" width="340" height="580" fill="#170C05" stroke="#000000" strokeWidth="7" />
          {/* Estantes con libros encuadernados */}
          {[0, 1, 2, 3, 4].map((row) => (
            <g key={`shelf-${row}`} transform={`translate(0, ${row * 110 + 20})`}>
              <rect x="10" y="90" width="320" height="14" fill="#3D2110" stroke="#000000" strokeWidth="3" />
              {/* Libros en el estante */}
              {Array.from({ length: 15 }).map((_, b) => {
                const bookWidth = 16 + ((b * 7) % 8);
                const bookHeight = 70 + ((b * 11) % 18);
                const colors = ["#7F1D1D", "#1E3A8A", "#064E3B", "#78350F", "#4C1D95", "#854D0E"];
                const color = colors[(row * 3 + b) % colors.length];
                return (
                  <rect
                    key={`book-${row}-${b}`}
                    x={20 + b * 20}
                    y={90 - bookHeight}
                    width={bookWidth}
                    height={bookHeight}
                    rx="2"
                    fill={color}
                    stroke="#000000"
                    strokeWidth="2.5"
                  />
                );
              })}
            </g>
          ))}
        </g>

        {/* 6. Reloj de pie antiguo con péndulo oscilante (Lado izquierdo, junto a ventana) */}
        <g transform="translate(490, 310)">
          {/* Caja del reloj */}
          <rect x="-26" y="0" width="52" height="380" rx="4" fill="#2E1C11" stroke="#000000" strokeWidth="5" />
          {/* Esfera del reloj */}
          <circle cx="0" cy="50" r="34" fill="#FEF3C7" stroke="#000000" strokeWidth="5" />
          <circle cx="0" cy="50" r="28" fill="none" stroke="#78350F" strokeWidth="2" />
          {/* Agujas marcando las 11:15 */}
          <line x1="0" y1="50" x2="-14" y2="35" stroke="#000000" strokeWidth="4" strokeLinecap="round" />
          <line x1="0" y1="50" x2="16" y2="40" stroke="#000000" strokeWidth="3" strokeLinecap="round" />
          <circle cx="0" cy="50" r="4" fill="#000000" />
          {/* Ventana de cristal del péndulo */}
          <rect x="-18" y="110" width="36" height="220" rx="3" fill="#0A0503" stroke="#78350F" strokeWidth="3" />
          {/* Péndulo oscilante con física suave */}
          <g transform={`translate(0, 120) rotate(${pendulumAngle})`}>
            <line x1="0" y1="0" x2="0" y2="160" stroke="#F59E0B" strokeWidth="4" />
            <circle cx="0" cy="160" r="18" fill="#F59E0B" stroke="#000000" strokeWidth="4" />
            <circle cx="0" cy="160" r="10" fill="#FEF08A" />
          </g>
        </g>

        {/* 7. Lámpara de escritorio de banquero en latón verde */}
        <g transform="translate(1420, 620)">
          {/* Cono de luz proyectada sobre la mesa */}
          <polygon points="0,-40 -260,260 260,260" fill="url(#deskLampCone)" />
          {/* Base y brazo de latón */}
          <line x1="0" y1="0" x2="0" y2="-40" stroke="#F59E0B" strokeWidth="8" strokeLinecap="round" />
          <path d="M 0 -40 Q 20 -70 -15 -85" fill="none" stroke="#F59E0B" strokeWidth="8" strokeLinecap="round" />
          {/* Tulipa de vidrio verde esmeralda */}
          <ellipse cx="-15" cy="-85" rx="38" ry="18" fill="#047857" stroke="#000000" strokeWidth="4" />
          <ellipse cx="-15" cy="-80" rx="32" ry="12" fill="#A7F3D0" opacity="0.8" />
        </g>
      </svg>
    </div>
  );
};

/**
 * Foreground del Despacho de Einstein (zIndex: 25).
 * Coloca la gran mesa de nogal macizo por delante del personaje sentado o actuando detrás.
 */
export const DespachoEinsteinForeground: React.FC<{ frame: number }> = () => {
  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden" style={{ zIndex: 25 }}>
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="einsteinDeskTopGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#451A03" />
            <stop offset="25%" stopColor="#290E02" />
            <stop offset="100%" stopColor="#140601" />
          </linearGradient>
        </defs>

        {/* Gran escritorio de madera de nogal macizo */}
        <g transform="translate(180, 710)">
          {/* Sombra proyectada bajo el escritorio */}
          <rect x="-20" y="240" width="1600" height="60" fill="#050201" opacity="0.75" />
          {/* Tablero superior con bisel y brillo neo-brutalista */}
          <polygon points="-40,0 1560,0 1520,70 -80,70" fill="url(#einsteinDeskTopGrad)" stroke="#000000" strokeWidth="7" />
          <line x1="-30" y1="6" x2="1550" y2="6" stroke="#9A3412" strokeWidth="3" opacity="0.7" />

          {/* Faldón frontal y cajones */}
          <rect x="-60" y="70" width="1560" height="230" fill="#240D04" stroke="#000000" strokeWidth="8" />
          {/* Cajones laterales */}
          <rect x="-30" y="90" width="340" height="90" fill="#1C0902" stroke="#000000" strokeWidth="5" />
          <circle cx="140" cy="135" r="9" fill="#F59E0B" stroke="#000000" strokeWidth="3" />
          <rect x="-30" y="195" width="340" height="85" fill="#1C0902" stroke="#000000" strokeWidth="5" />
          <circle cx="140" cy="237" r="9" fill="#F59E0B" stroke="#000000" strokeWidth="3" />

          <rect x="1130" y="90" width="340" height="90" fill="#1C0902" stroke="#000000" strokeWidth="5" />
          <circle cx="1300" cy="135" r="9" fill="#F59E0B" stroke="#000000" strokeWidth="3" />
          <rect x="1130" y="195" width="340" height="85" fill="#1C0902" stroke="#000000" strokeWidth="5" />
          <circle cx="1300" cy="237" r="9" fill="#F59E0B" stroke="#000000" strokeWidth="3" />

          {/* Manuscritos manuscritos sobre la mesa con fórmulas matemáticas */}
          <g transform="translate(460, -18) rotate(-4)">
            <rect x="0" y="0" width="220" height="95" rx="3" fill="#FEF3C7" stroke="#000000" strokeWidth="4" />
            <line x1="20" y1="20" x2="200" y2="20" stroke="#78350F" strokeWidth="3" strokeDasharray="14 6" />
            <line x1="20" y1="36" x2="180" y2="36" stroke="#78350F" strokeWidth="3" strokeDasharray="10 5" />
            <text x="30" y="65" fill="#991B1B" fontSize="18" fontWeight="bold" fontFamily="'Courier New', monospace">
              R_μν = 0 (VACÍO)
            </text>
          </g>

          <g transform="translate(710, -26) rotate(6)">
            <rect x="0" y="0" width="240" height="105" rx="3" fill="#FFFBEB" stroke="#000000" strokeWidth="4" />
            <text x="25" y="32" fill="#1E3A8A" fontSize="15" fontWeight="900" fontFamily="'Times New Roman', serif">
              Zur allgemeinen Relativitätstheorie
            </text>
            <line x1="25" y1="48" x2="215" y2="48" stroke="#334155" strokeWidth="2.5" strokeDasharray="8 4" />
            <line x1="25" y1="64" x2="195" y2="64" stroke="#334155" strokeWidth="2.5" strokeDasharray="12 4" />
            <circle cx="180" cy="82" r="12" fill="none" stroke="#DC2626" strokeWidth="2.5" />
            <text x="180" y="86" textAnchor="middle" fill="#DC2626" fontSize="11" fontWeight="bold">r_s</text>
          </g>

          {/* Tintero victoriano y pluma de ganso */}
          <g transform="translate(1040, -14)">
            <rect x="0" y="0" width="46" height="42" rx="6" fill="#1E293B" stroke="#000000" strokeWidth="4" />
            <ellipse cx="23" cy="6" rx="14" ry="7" fill="#000000" />
            {/* Pluma blanca en diagonal */}
            <path d="M 23 4 Q 45 -45 90 -85 Q 80 -45 35 15 Z" fill="#F8FAFC" stroke="#000000" strokeWidth="3.5" />
            <line x1="23" y1="4" x2="88" y2="-82" stroke="#CBD5E1" strokeWidth="2" />
          </g>

          {/* Lupa de bronce para examinar cálculos */}
          <g transform="translate(360, 10) rotate(-22)">
            <circle cx="0" cy="0" r="30" fill="rgba(224,242,254,0.35)" stroke="#F59E0B" strokeWidth="6" />
            <line x1="22" y1="22" x2="65" y2="65" stroke="#78350F" strokeWidth="8" strokeLinecap="round" />
            <line x1="22" y1="22" x2="65" y2="65" stroke="#F59E0B" strokeWidth="4" strokeLinecap="round" />
          </g>
        </g>
      </svg>
    </div>
  );
};

/**
 * Escenario 2: Disco de Acreción Cinemático (Agujero Negro Supermasivo).
 * Vista de horizonte de sucesos con efecto de lente gravitacional, asimetría Doppler relativista,
 * halo de fotones brillante y chorros de plasma polar.
 */
export const DiscoAcrecionStage: React.FC<{ frame: number }> = ({ frame }) => {
  const rotation = (frame * 0.28) % 360;
  const pulse = Math.sin(frame * 0.14) * 2.0;
  const jetFlicker = 0.85 + Math.sin(frame * 0.24) * 0.15;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#020308] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="bhVoidGrad" cx="0.5" cy="0.5" r="0.5">
            <stop offset="0%" stopColor="#000000" />
            <stop offset="85%" stopColor="#000000" />
            <stop offset="100%" stopColor="#0F172A" stopOpacity="0.8" />
          </radialGradient>
          <linearGradient id="dopplerDiskGrad" x1="0" y1="0" x2="1" y2="0">
            {/* Lado izquierdo azulado / Doppler azul brillante (se acerca al observador) */}
            <stop offset="0%" stopColor="#0284C7" stopOpacity="0" />
            <stop offset="15%" stopColor="#38BDF8" stopOpacity="0.85" />
            <stop offset="35%" stopColor="#FACC15" stopOpacity="0.95" />
            <stop offset="50%" stopColor="#FB923C" stopOpacity="0.9" />
            {/* Lado derecho enrojecido / Doppler rojo atenuado (se aleja) */}
            <stop offset="75%" stopColor="#DC2626" stopOpacity="0.6" />
            <stop offset="100%" stopColor="#7F1D1D" stopOpacity="0" />
          </linearGradient>
          <radialGradient id="photonRingGrad" cx="0.5" cy="0.5" r="0.5">
            <stop offset="85%" stopColor="#000000" />
            <stop offset="92%" stopColor="#FDE047" />
            <stop offset="97%" stopColor="#38BDF8" />
            <stop offset="100%" stopColor="#000000" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* 1. Fondo de cielo profundo con polvo estelar y cúmulos lejanos */}
        <rect x="0" y="0" width="1920" height="1080" fill="#02040A" />
        {Array.from({ length: 60 }).map((_, i) => (
          <circle
            key={`bh-star-${i}`}
            cx={(i * 32.7) % 1920}
            cy={(i * 59.3) % 1080}
            r={(i % 3) * 0.7 + 1}
            fill={i % 4 === 0 ? "#38BDF8" : i % 5 === 0 ? "#FDE047" : "#FFFFFF"}
            opacity={0.4 + Math.sin(frame * 0.12 + i) * 0.3}
          />
        ))}

        {/* 2. Chorros relativistas polares de plasma que salen a velocidades lumínicas */}
        <g transform="translate(960, 520)">
          {/* Chorro Superior */}
          <polygon
            points={`-24,0 -120,-600 120,-600 24,0`}
            fill="#38BDF8"
            opacity={0.12 * jetFlicker}
          />
          <line x1="0" y1="-100" x2="0" y2="-620" stroke="#0EA5E9" strokeWidth="8" opacity={0.65 * jetFlicker} />
          <line x1="0" y1="-120" x2="0" y2="-580" stroke="#E0F2FE" strokeWidth="3" opacity={0.9 * jetFlicker} />

          {/* Chorro Inferior */}
          <polygon
            points={`-24,0 -120,600 120,600 24,0`}
            fill="#38BDF8"
            opacity={0.12 * jetFlicker}
          />
          <line x1="0" y1="100" x2="0" y2="620" stroke="#0EA5E9" strokeWidth="8" opacity={0.65 * jetFlicker} />
          <line x1="0" y1="120" x2="0" y2="580" stroke="#E0F2FE" strokeWidth="3" opacity={0.9 * jetFlicker} />
        </g>

        {/* 3. Halo curvado superior del disco de acreción (Efecto Lente Gravitacional de Einstein) */}
        <g transform="translate(960, 520)">
          {/* Lente gravitacional proyectando la cara trasera del disco por encima del horizonte */}
          <ellipse
            cx="0"
            cy="-110"
            rx="540"
            ry="240"
            fill="none"
            stroke="url(#dopplerDiskGrad)"
            strokeWidth="85"
            strokeDasharray="40 10"
            opacity="0.82"
            transform={`rotate(${Math.sin(rotation * 0.05) * 4})`}
          />
          {/* Lente inferior */}
          <ellipse
            cx="0"
            cy="110"
            rx="490"
            ry="200"
            fill="none"
            stroke="url(#dopplerDiskGrad)"
            strokeWidth="70"
            strokeDasharray="30 8"
            opacity="0.72"
            transform={`rotate(${Math.sin(rotation * 0.05) * -4})`}
          />
        </g>

        {/* 4. Disco de acreción frontal ecuatorial con rotación y turbulencia plasmática */}
        <g transform="translate(960, 520)">
          <ellipse
            cx="0"
            cy="0"
            rx="780"
            ry="180"
            fill="none"
            stroke="url(#dopplerDiskGrad)"
            strokeWidth="110"
            strokeDasharray="24 12"
            opacity="0.9"
            style={{ filter: "drop-shadow(0 0 45px #F59E0B)" }}
          />
          {/* Anillos concéntricos de filamentos de gas a 10 millones de grados Kelvin */}
          <ellipse
            cx="0"
            cy="0"
            rx="640"
            ry="140"
            fill="none"
            stroke="#FEF08A"
            strokeWidth="18"
            strokeDasharray="14 10"
            opacity="0.75"
          />
          <ellipse
            cx="-120"
            cy="0"
            rx="460"
            ry="105"
            fill="none"
            stroke="#38BDF8"
            strokeWidth="24"
            opacity="0.85"
            style={{ filter: "drop-shadow(-20px 0 35px #0284C7)" }}
          />
        </g>

        {/* 5. La Sombra Central del Agujero Negro y la Esfera de Fotones (Photon Sphere) */}
        <g transform="translate(960, 520)">
          {/* Esfera de fotones (r = 1.5 rs): Anillo de luz ultradelgado e intenso */}
          <circle
            cx="0"
            cy="0"
            r={240 + pulse}
            fill="none"
            stroke="#FEF08A"
            strokeWidth="10"
            strokeDasharray="22 8"
            opacity="0.95"
            style={{ filter: "drop-shadow(0 0 25px #FDE047)" }}
          />
          <circle
            cx="0"
            cy="0"
            r={235 + pulse}
            fill="none"
            stroke="#38BDF8"
            strokeWidth="4"
            opacity="0.9"
          />

          {/* Sombra del Agujero Negro: Oscuridad absoluta e impenetrable */}
          <circle
            cx="0"
            cy="0"
            r={228 + pulse}
            fill="#000000"
            stroke="#000000"
            strokeWidth="6"
          />
        </g>

        {/* 6. Plataforma de observación cinemática en tercio inferior */}
        <g transform="translate(0, 930)">
          <rect x="0" y="0" width="1920" height="150" fill="#0B132B" stroke="#000000" strokeWidth="7" />
          <line x1="0" y1="20" x2="1920" y2="20" stroke="#38BDF8" strokeWidth="4" />
          {/* Barandilla de seguridad con marcas métricas */}
          {Array.from({ length: 16 }).map((_, i) => (
            <line
              key={`railing-${i}`}
              x1={i * 128 + 64}
              y1="0"
              x2={i * 128 + 64}
              y2="60"
              stroke="#1E293B"
              strokeWidth="5"
            />
          ))}
          <text x="960" y="85" textAnchor="middle" fill="#38BDF8" fontSize="20" fontWeight="900" fontFamily="'Arial Black', sans-serif" letterSpacing="4">
            ZONA DE OBSERVACIÓN ORBITAL: DISTANCIA SEGURA R = 10 R_S
          </text>
        </g>
      </svg>
    </div>
  );
};

/**
 * Escenario 3: Horizonte de Sucesos y Distorsión Extrema del Espacio-Tiempo.
 * Perspectiva cayendo hacia la superficie unidireccional (r = 2GM/c²).
 * La malla geométrica se precipita hacia el abismo central y los conos de luz se inclinan.
 */
export const HorizonteSucesosStage: React.FC<{ frame: number }> = ({ frame }) => {
  const fallProgress = (frame * 1.5) % 60;
  const pulseGrid = Math.sin(frame * 0.16) * 2.2;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#05050C] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="horizonteAbyssGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0284C7" stopOpacity="0.4" />
            <stop offset="45%" stopColor="#7C3AED" stopOpacity="0.6" />
            <stop offset="80%" stopColor="#DC2626" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#000000" />
          </linearGradient>
          <radialGradient id="eventHorizonCenter" cx="0.5" cy="0.65" r="0.55">
            <stop offset="0%" stopColor="#000000" />
            <stop offset="65%" stopColor="#000000" />
            <stop offset="85%" stopColor="#DC2626" stopOpacity="0.7" />
            <stop offset="95%" stopColor="#38BDF8" stopOpacity="0.85" />
            <stop offset="100%" stopColor="#000000" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* 1. Fondo cósmico distorsionado por corrimiento al rojo gravitacional */}
        <rect x="0" y="0" width="1920" height="1080" fill="url(#horizonteAbyssGrad)" />

        {/* 2. Malla geométrica de Minkowski deformándose en embudo hiperbólico */}
        <g transform="translate(960, 680)">
          {/* Círculos concéntricos de coordenadas 'r' que se comprimen hacia el horizonte */}
          {[120, 220, 340, 480, 650, 840, 1050].map((radius, idx) => {
            const currentR = radius + fallProgress;
            return (
              <ellipse
                key={`grid-r-${idx}`}
                cx="0"
                cy="0"
                rx={currentR}
                ry={currentR * 0.42}
                fill="none"
                stroke={idx < 2 ? "#DC2626" : idx < 4 ? "#F59E0B" : "#22D3EE"}
                strokeWidth={idx < 2 ? "5" : "3"}
                strokeDasharray="16 10"
                opacity={0.4 + (idx * 0.08)}
              />
            );
          })}

          {/* Líneas geodésicas radiales convergiendo en la garganta gravitacional */}
          {Array.from({ length: 24 }).map((_, i) => {
            const angle = (i * 15 * Math.PI) / 180;
            const x1 = Math.cos(angle) * 1100;
            const y1 = Math.sin(angle) * 460;
            const x0 = Math.cos(angle) * 70;
            const y0 = Math.sin(angle) * 30;
            return (
              <line
                key={`geo-${i}`}
                x1={x1}
                y1={y1}
                x2={x0}
                y2={y0}
                stroke={i % 2 === 0 ? "#38BDF8" : "#818CF8"}
                strokeWidth="2.5"
                strokeDasharray="12 8"
                opacity="0.55"
              />
            );
          })}

          {/* La garganta del Horizonte de Sucesos (r = 2GM/c²) */}
          <ellipse
            cx="0"
            cy="0"
            rx={160 + pulseGrid}
            ry={(160 + pulseGrid) * 0.42}
            fill="#000000"
            stroke="#DC2626"
            strokeWidth="8"
            style={{ filter: "drop-shadow(0 0 35px #EF4444)" }}
          />
          <text x="0" y="8" textAnchor="middle" fill="#FFFFFF" fontSize="16" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            HORIZONTE: r = r_s
          </text>
        </g>

        {/* 3. Conos de luz inclinándose a lo largo de la trayectoria de caída */}
        {/* Cono 1: Lejos del horizonte (Vertical - Puede escapar hacia el futuro) */}
        <g transform="translate(360, 280)">
          <ellipse cx="0" cy="-40" rx="42" ry="14" fill="#0284C7" opacity="0.35" stroke="#38BDF8" strokeWidth="2.5" />
          <line x1="-42" y1="-40" x2="0" y2="40" stroke="#38BDF8" strokeWidth="3" />
          <line x1="42" y1="-40" x2="0" y2="40" stroke="#38BDF8" strokeWidth="3" />
          <circle cx="0" cy="40" r="5" fill="#38BDF8" />
          <rect x="-60" y="55" width="120" height="24" rx="4" fill="#0F172A" stroke="#38BDF8" strokeWidth="2" />
          <text x="0" y="71" textAnchor="middle" fill="#38BDF8" fontSize="11" fontWeight="bold">r &gt; 2r_s (ESCAPABLE)</text>
        </g>

        {/* Cono 2: En la frontera r = 2GM/c² (Inclinado a 45° - La luz sólo puede permanecer en el borde) */}
        <g transform="translate(740, 420) rotate(35)">
          <ellipse cx="0" cy="-40" rx="42" ry="14" fill="#D97706" opacity="0.45" stroke="#FBBF24" strokeWidth="2.5" />
          <line x1="-42" y1="-40" x2="0" y2="40" stroke="#FBBF24" strokeWidth="3" />
          <line x1="42" y1="-40" x2="0" y2="40" stroke="#FBBF24" strokeWidth="3" />
          <circle cx="0" cy="40" r="5" fill="#FBBF24" />
          <g transform="rotate(-35)">
            <rect x="-65" y="55" width="130" height="24" rx="4" fill="#1C1917" stroke="#FBBF24" strokeWidth="2" />
            <text x="0" y="71" textAnchor="middle" fill="#FBBF24" fontSize="11" fontWeight="bold">r = r_s (CRÍTICO 45°)</text>
          </g>
        </g>

        {/* Cono 3: En el interior r < 2GM/c² (Completamente volcado hacia adentro - Futuro = Centro) */}
        <g transform="translate(1080, 520) rotate(80)">
          <ellipse cx="0" cy="-40" rx="42" ry="14" fill="#DC2626" opacity="0.55" stroke="#EF4444" strokeWidth="3" />
          <line x1="-42" y1="-40" x2="0" y2="40" stroke="#EF4444" strokeWidth="3.5" />
          <line x1="42" y1="-40" x2="0" y2="40" stroke="#EF4444" strokeWidth="3.5" />
          <circle cx="0" cy="40" r="5" fill="#EF4444" />
          <g transform="rotate(-80)">
            <rect x="-70" y="55" width="140" height="24" rx="4" fill="#180404" stroke="#EF4444" strokeWidth="2" />
            <text x="0" y="71" textAnchor="middle" fill="#EF4444" fontSize="11" fontWeight="bold">r &lt; r_s (INELUDIBLE r=0)</text>
          </g>
        </g>

        {/* 4. Letrero de Advertencia Relativista Superior */}
        <g transform="translate(960, 90)">
          <rect x="-340" y="-35" width="680" height="70" rx="8" fill="#180706" stroke="#EF4444" strokeWidth="4" />
          <text x="0" y="-8" textAnchor="middle" fill="#EF4444" fontSize="22" fontWeight="900" fontFamily="'Arial Black', sans-serif" letterSpacing="2">
            ZONA DE NO RETORNO: VELOCIDAD DE ESCAPE &gt; C
          </text>
          <text x="0" y="20" textAnchor="middle" fill="#FCA5A5" fontSize="14" fontWeight="bold" fontFamily="'Courier New', monospace">
            EL ESPACIO Y EL TIEMPO INTERCAMBIAN SUS PAPELES MATEMÁTICOS
          </text>
        </g>
      </svg>
    </div>
  );
};

/**
 * Escenario 4: Vacío de la Singularidad Cuántica (r → 0).
 * El corazón del colapso donde las ecuaciones de Einstein divergen a infinito
 * y la geometría se desintegra en espuma cuántica de Planck y redes de espín.
 */
export const VacioSingularidadStage: React.FC<{ frame: number }> = ({ frame }) => {
  const quantumChaos = Math.sin(frame * 0.20) * 3;
  const loopPulse = 0.8 + Math.sin(frame * 0.15) * 0.2;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#07010B] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="singularityCoreGrad" cx="0.5" cy="0.5" r="0.5">
            <stop offset="0%" stopColor="#FFFFFF" />
            <stop offset="20%" stopColor="#38BDF8" />
            <stop offset="55%" stopColor="#818CF8" />
            <stop offset="80%" stopColor="#C084FC" stopOpacity="0.8" />
            <stop offset="100%" stopColor="#07010B" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* 1. Fondo de vacío primordial con fragmentos fractales de espaciotiempo roto */}
        <rect x="0" y="0" width="1920" height="1080" fill="#050109" />

        {/* 2. Red de Espín (Spin Network / Gravedad Cuántica de Bucles) */}
        <g transform="translate(960, 540)">
          {/* Nodos de Planck interconectados con enlaces cuánticos */}
          {[
            { x: -480, y: -260 },
            { x: -280, y: -380 },
            { x: 220, y: -340 },
            { x: 520, y: -210 },
            { x: 620, y: 140 },
            { x: 380, y: 320 },
            { x: -140, y: 360 },
            { x: -540, y: 220 },
            { x: -320, y: -40 },
            { x: 310, y: 40 },
            { x: -60, y: -180 },
            { x: 120, y: 220 },
          ].map((pt, i, arr) => {
            const next = arr[(i + 1) % arr.length];
            const cross = arr[(i + 5) % arr.length];
            return (
              <g key={`spin-node-${i}`}>
                {/* Enlace al siguiente nodo */}
                <line
                  x1={pt.x}
                  y1={pt.y}
                  x2={next.x}
                  y2={next.y}
                  stroke="#A855F7"
                  strokeWidth="3"
                  strokeDasharray="8 6"
                  opacity={0.7}
                />
                {/* Enlace transversal de entrelazamiento */}
                <line
                  x1={pt.x}
                  y1={pt.y}
                  x2={cross.x}
                  y2={cross.y}
                  stroke="#38BDF8"
                  strokeWidth="1.8"
                  strokeDasharray="4 4"
                  opacity={0.45 * loopPulse}
                />
                {/* Vértice cuántico de Planck (j = 1/2) */}
                <circle
                  cx={pt.x}
                  cy={pt.y}
                  r={8 + (i % 3) * 2}
                  fill="#C084FC"
                  stroke="#000000"
                  strokeWidth="3"
                />
                <circle cx={pt.x} cy={pt.y} r={3} fill="#FFFFFF" />
              </g>
            );
          })}

          {/* Lazos cerrados de bucle cuántico (Wilson Loops) */}
          {[-1, 1].map((dir, idx) => (
            <ellipse
              key={`wilson-${idx}`}
              cx={dir * 260}
              cy={dir * -90}
              rx={180}
              ry={90}
              fill="none"
              stroke="#22D3EE"
              strokeWidth="4"
              strokeDasharray="18 10"
              transform={`rotate(${dir * (frame * 0.35 + 25)})`}
              opacity="0.8"
            />
          ))}

          {/* 3. La Singularidad Central: El Núcleo de Densidad y Curvatura Infinita */}
          {/* Ondas gravitacionales cuánticas de choque */}
          {[140, 240, 360, 490].map((r, i) => (
            <circle
              key={`shockwave-${i}`}
              cx="0"
              cy="0"
              r={r + ((frame * 2.5 + i * 50) % 200)}
              fill="none"
              stroke={i % 2 === 0 ? "#E879F9" : "#38BDF8"}
              strokeWidth={4 - i * 0.7}
              opacity={0.8 - (i * 0.18)}
            />
          ))}

          {/* Resplandor hiperbólico de la singularidad */}
          <circle
            cx={quantumChaos}
            cy={-quantumChaos}
            r={130}
            fill="url(#singularityCoreGrad)"
          />

          {/* Punto de singularidad matemática r = 0 */}
          <circle cx="0" cy="0" r={16} fill="#FFFFFF" stroke="#000000" strokeWidth="4" />
          <circle cx="0" cy="0" r={7} fill="#38BDF8" />

          {/* Fórmulas matemáticas de ruptura gravitacional en el espacio */}
          <text x="0" y="-160" textAnchor="middle" fill="#F43F5E" fontSize="32" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            CURVATURA RIEMANN → ∞
          </text>
          <text x="0" y="190" textAnchor="middle" fill="#38BDF8" fontSize="24" fontWeight="bold" fontFamily="'Courier New', monospace">
            VOLUMEN = 0  |  DENSIDAD = ∞  |  1/0 = INDEFINIDO
          </text>
        </g>

        {/* 4. Rótulo inferior de Gravedad Cuántica */}
        <g transform="translate(960, 980)">
          <rect x="-380" y="-32" width="760" height="64" rx="8" fill="#1E062B" stroke="#A855F7" strokeWidth="4" />
          <text x="0" y="8" textAnchor="middle" fill="#E9D5FF" fontSize="20" fontWeight="900" fontFamily="'Arial Black', sans-serif" letterSpacing="2">
            ESCALA DE PLANCK (1.616 × 10⁻³⁵ METROS): LA RELATIVIDAD COLAPSA
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 1. Acantilado Costero bajo Tormenta (Escena 1) */
export const AcantiladoTormentaCosteraStage: React.FC<{ frame: number }> = ({ frame }) => {
  const windOffset = (frame * 24) % 1920;
  const seaWave = Math.sin(frame * 0.12) * 14;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0A0D1A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="stormSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E1B4B" />
            <stop offset="60%" stopColor="#0F172A" />
            <stop offset="100%" stopColor="#090D16" />
          </linearGradient>
          <linearGradient id="seaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0284C7" />
            <stop offset="40%" stopColor="#0369A1" />
            <stop offset="100%" stopColor="#020617" />
          </linearGradient>
        </defs>

        {/* Cielo de tormenta encapotado */}
        <rect x="0" y="0" width="1920" height="740" fill="url(#stormSky)" />

        {/* Nubes turbulentas de cizalladura en capas */}
        {[-1, 0, 1].map((cloudRow, i) => (
          <path
            key={`cloud-${i}`}
            d={`M -200 ${220 + i * 110} Q 400 ${180 + i * 90 + Math.sin(frame * 0.05 + i) * 20} 960 ${240 + i * 100} Q 1500 ${200 + i * 80} 2120 ${230 + i * 90}`}
            fill="none"
            stroke="#312E81"
            strokeWidth="80"
            strokeOpacity="0.4"
          />
        ))}

        {/* Océano encrespado con oleaje y espuma */}
        <polygon
          points={`0,${740 + seaWave} 1920,${740 - seaWave} 1920,1080 0,1080`}
          fill="url(#seaGrad)"
        />
        <line x1="0" y1="740" x2="1920" y2="740" stroke="#38BDF8" strokeWidth="4" strokeDasharray="12 6" />

        {/* Acantilado rocoso a la izquierda */}
        <polygon
          points="0,320 280,480 340,620 420,780 460,1080 0,1080"
          fill="#0F172A"
          stroke="#000000"
          strokeWidth="6"
        />
        <polygon points="0,350 240,490 280,630 360,820 380,1080 0,1080" fill="#1E293B" />

        {/* Vectores dinámicos de viento turbulento (azul y violeta) cruzando el encuadre */}
        {[180, 290, 420, 560, 680].map((yLine, idx) => (
          <line
            key={`wind-${idx}`}
            x1={(windOffset + idx * 380) % 2200 - 200}
            y1={yLine}
            x2={(windOffset + idx * 380) % 2200 + 260}
            y2={yLine + Math.sin(frame * 0.15 + idx) * 12}
            stroke={idx % 2 === 0 ? "#38BDF8" : "#818CF8"}
            strokeWidth="3.5"
            strokeDasharray="18 10"
            opacity="0.75"
          />
        ))}

        {/* Rótulo de altitud y condiciones climáticas */}
        <g transform="translate(1480, 80)">
          <rect width="360" height="54" rx="8" fill="#000000" stroke="#818CF8" strokeWidth="3" />
          <circle cx="28" cy="27" r="8" fill="#EF4444" className="animate-pulse" />
          <text x="50" y="34" fill="#F8FAFC" fontSize="16" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            TURBULENCIA DE CIZALLADURA
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 2. Túnel de Viento Aerodinámico Industrial (Escenas 2, 4, 6) */
export const TunelVientoIndustrialStage: React.FC<{ frame: number }> = ({ frame }) => {
  const fanRot = frame * 12;
  // Flujo continuo de DERECHA a IZQUIERDA con menor opacidad para sensación de viento fluido
  const streamOffset = 2300 - ((frame * 26) % 2300);

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B111E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="tunnelGlass" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E293B" stopOpacity="0.8" />
            <stop offset="50%" stopColor="#0F172A" stopOpacity="0.2" />
            <stop offset="100%" stopColor="#0B111E" stopOpacity="0.9" />
          </linearGradient>
          <linearGradient id="metalIntake" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stopColor="#475569" />
            <stop offset="100%" stopColor="#1E293B" />
          </linearGradient>
        </defs>

        {/* Estructura general de la cámara del túnel de viento */}
        <rect x="0" y="0" width="1920" height="820" fill="url(#tunnelGlass)" />

        {/* Tobera de admisión metálica (izquierda) con panal enderezador de flujo */}
        <polygon points="0,120 220,240 220,700 0,820" fill="url(#metalIntake)" stroke="#000000" strokeWidth="5" />
        {/* Rejilla de panal */}
        {Array.from({ length: 9 }).map((_, i) => (
          <line key={`honey-${i}`} x1="220" y1={250 + i * 50} x2="260" y2={250 + i * 50} stroke="#64748B" strokeWidth="3" />
        ))}

        {/* Difusor de salida con rotor de turbina (derecha) */}
        <polygon points="1700,240 1920,120 1920,820 1700,700" fill="url(#metalIntake)" stroke="#000000" strokeWidth="5" />
        <g transform={`translate(1820, 470) rotate(${fanRot})`}>
          <circle cx="0" cy="0" r="32" fill="#0F172A" stroke="#38BDF8" strokeWidth="4" />
          {[0, 60, 120, 180, 240, 300].map((ang) => (
            <line
              key={`blade-${ang}`}
              x1="0"
              y1="0"
              x2={Math.cos((ang * Math.PI) / 180) * 110}
              y2={Math.sin((ang * Math.PI) / 180) * 110}
              stroke="#64748B"
              strokeWidth="12"
              strokeLinecap="round"
            />
          ))}
        </g>

        {/* Suelo de laboratorio con franjas de seguridad industriales */}
        <rect x="0" y="820" width="1920" height="260" fill="#0F172A" />
        <line x1="0" y1="820" x2="1920" y2="820" stroke="#000000" strokeWidth="6" />

        {/* Franja de precaución amarillo/negro */}
        {Array.from({ length: 24 }).map((_, i) => (
          <polygon
            key={`hazard-${i}`}
            points={`${i * 85},820 ${i * 85 + 40},820 ${i * 85},850 ${i * 85 - 40},850`}
            fill="#FFE600"
          />
        ))}

        {/* Líneas de corriente de humo blanco fluyendo de DERECHA a IZQUIERDA con baja opacidad aerodinámica */}
        {[280, 340, 400, 460, 520, 580, 640, 700].map((yStream, sIdx) => {
          const xPos = (streamOffset + sIdx * 290) % 2300 - 250;
          return (
            <line
              key={`smoke-${sIdx}`}
              x1={xPos + 480}
              y1={yStream}
              x2={xPos}
              y2={yStream}
              stroke="#F8FAFC"
              strokeWidth="2.2"
              strokeDasharray="24 14"
              opacity="0.28"
            />
          );
        })}

        {/* Escala de medición métrica en vidrio */}
        <g transform="translate(420, 190)">
          <rect width="1080" height="34" rx="4" fill="#000000" fillOpacity="0.7" stroke="#38BDF8" strokeWidth="2" />
          {Array.from({ length: 11 }).map((_, mIdx) => (
            <g key={`m-${mIdx}`} transform={`translate(${mIdx * 100 + 40}, 0)`}>
              <line x1="0" y1="0" x2="0" y2="14" stroke="#38BDF8" strokeWidth="2" />
              <text x="0" y="24" textAnchor="middle" fill="#38BDF8" fontSize="10" fontFamily="'Arial Black', sans-serif" fontWeight="900">
                {`${(mIdx - 5) * 20} CM`}
              </text>
            </g>
          ))}
        </g>
      </svg>
    </div>
  );
};

/** 3. Espacio Técnico de Dinámica de Fluidos CFD (Escena 3) */
export const EspacioCfdTecnicoStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#040A17] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <pattern id="cfdGrid" width="60" height="60" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="60" y2="0" stroke="#1E293B" strokeWidth="1" />
            <line x1="0" y1="0" x2="0" y2="60" stroke="#1E293B" strokeWidth="1" />
          </pattern>
        </defs>

        {/* Cuadrícula de diseño aerodinámico */}
        <rect x="0" y="0" width="1920" height="1080" fill="url(#cfdGrid)" />

        {/* Isobaras de presión aerodinámica en gradiente */}
        {[
          { cx: 960, cy: 380, rx: 580, ry: 190, stroke: "#38BDF8" },
          { cx: 960, cy: 400, rx: 460, ry: 140, stroke: "#10B981" },
          { cx: 960, cy: 480, rx: 380, ry: 100, stroke: "#F59E0B" },
          { cx: 960, cy: 540, rx: 280, ry: 70, stroke: "#EF4444" },
        ].map((iso, i) => (
          <ellipse
            key={`iso-${i}`}
            cx={iso.cx}
            cy={iso.cy}
            rx={iso.rx}
            ry={iso.ry}
            fill="none"
            stroke={iso.stroke}
            strokeWidth="2"
            strokeDasharray="8 6"
            strokeOpacity="0.45"
          />
        ))}

        {/* Barra de escala cromática de presión CFD a la izquierda */}
        <g transform="translate(80, 280)">
          <rect width="36" height="420" rx="6" fill="#000000" stroke="#334155" strokeWidth="3" />
          {["#EF4444", "#F59E0B", "#FFE600", "#10B981", "#38BDF8", "#1E40AF"].map((col, cIdx) => (
            <rect key={`bar-${cIdx}`} x="4" y={6 + cIdx * 68} width="28" height="64" fill={col} rx="2" />
          ))}
          <text x="48" y="24" fill="#EF4444" fontSize="12" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            +CP (ALTA PRESIÓN)
          </text>
          <text x="48" y="415" fill="#38BDF8" fontSize="12" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            -CP (SUCCIÓN)
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 4. Entorno Macro-Anatómico Osteomuscular del Ala (Escenas 5, 8) */
export const AnatomiaMacroAlaStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#070D18] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="macroGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#0284C7" stopOpacity="0.25" />
            <stop offset="100%" stopColor="#070D18" stopOpacity="0" />
          </radialGradient>
        </defs>

        <rect x="0" y="0" width="1920" height="1080" fill="#070D18" />
        <circle cx="960" cy="540" r="650" fill="url(#macroGlow)" />

        {/* Silueta radiográfica del esqueleto alar aviar */}
        <g transform="translate(380, 460)">
          {/* Húmero */}
          <path d="M 0 0 C 80 -40, 200 -30, 280 20" fill="none" stroke="#67E8F9" strokeWidth="18" strokeLinecap="round" opacity="0.6" />
          {/* Radio y Cúbito paralelos */}
          <path d="M 280 20 C 380 40, 540 60, 680 50" fill="none" stroke="#67E8F9" strokeWidth="12" strokeLinecap="round" opacity="0.55" />
          <path d="M 280 38 C 380 62, 540 82, 680 72" fill="none" stroke="#67E8F9" strokeWidth="10" strokeLinecap="round" opacity="0.45" />
          {/* Mano y primer dedo (Álula) */}
          <path d="M 680 50 L 760 10" fill="none" stroke="#FFE600" strokeWidth="12" strokeLinecap="round" />
          <circle cx="760" cy="10" r="10" fill="#FFE600" />
          <text x="740" y="-12" fill="#FFE600" fontSize="16" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            DEDO I (ÁLULA)
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 5. Espacio Nanoscópico de Microscopía Electrónica SEM (Escena 7) */
export const NanoscopiaSemQueratinaStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#060709] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Líneas de barrido raster de microscopio electrónico */}
        {Array.from({ length: 27 }).map((_, i) => (
          <line
            key={`sem-scan-${i}`}
            x1="0"
            y1={i * 40}
            x2="1920"
            y2={i * 40}
            stroke="#1E293B"
            strokeWidth="0.8"
            strokeOpacity="0.4"
          />
        ))}

        {/* Fibras transversales de queratina en nanoscopía */}
        {[-3, -2, -1, 0, 1, 2, 3].map((pos) => (
          <path
            key={`fiber-${pos}`}
            d={`M ${pos * 240 + 960} -50 C ${pos * 260 + 980} 500, ${pos * 200 + 920} 800, ${pos * 240 + 960} 1150`}
            fill="none"
            stroke="#334155"
            strokeWidth="28"
            strokeOpacity="0.3"
          />
        ))}

        {/* Indicador de escala nanométrica en esquina inferior derecha */}
        <g transform="translate(1500, 960)">
          <rect width="320" height="54" rx="6" fill="#000000" stroke="#94A3B8" strokeWidth="2" />
          <line x1="20" y1="27" x2="160" y2="27" stroke="#FFFFFF" strokeWidth="4" />
          <line x1="20" y1="20" x2="20" y2="34" stroke="#FFFFFF" strokeWidth="3" />
          <line x1="160" y1="20" x2="160" y2="34" stroke="#FFFFFF" strokeWidth="3" />
          <text x="180" y="32" fill="#F8FAFC" fontSize="16" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            50.0 µm (SEM)
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 6. Laboratorio de Histología y Neurobiología Dérmica (Escenas 9, 10) */
export const LaboratorioHistologiaHerbstStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0C0614] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="dermisGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#4C0519" stopOpacity="0.4" />
            <stop offset="50%" stopColor="#1E1B4B" stopOpacity="0.6" />
            <stop offset="100%" stopColor="#020617" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="1920" height="1080" fill="url(#dermisGrad)" />

        {/* Estrato celular de la piel */}
        <line x1="0" y1="360" x2="1920" y2="360" stroke="#E11D48" strokeWidth="4" strokeDasharray="16 8" />
        <text x="60" y="340" fill="#FDA4AF" fontSize="18" fontFamily="'Arial Black', sans-serif" fontWeight="900">
          EPIDERMIS AVIAR
        </text>

        {/* Canales neuronales y axones en el estrato dérmico */}
        {[
          "M 200 480 Q 400 620 700 580 T 1300 700 T 1800 640",
          "M 150 620 Q 550 780 950 680 T 1550 820 T 1900 750",
          "M 100 800 Q 600 890 1100 820 T 1700 900",
        ].map((axon, idx) => (
          <path
            key={`axon-${idx}`}
            d={axon}
            fill="none"
            stroke="#FACC15"
            strokeWidth="3"
            strokeDasharray="12 6"
            strokeOpacity="0.5"
          />
        ))}
      </svg>
    </div>
  );
};

/** 7. Estudio Estroboscópico de Captura de Movimiento (Escena 11) */
export const EstudioEstroboscopicoCapturaStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#030305] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="strobeBeam" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#FFFFFF" stopOpacity="0.25" />
            <stop offset="100%" stopColor="#000000" stopOpacity="0" />
          </linearGradient>
        </defs>

        {/* Focos estroboscópicos cenitales proyectando conos de luz */}
        {[380, 960, 1540].map((spotX, i) => (
          <polygon
            key={`spot-${i}`}
            points={`${spotX - 40},0 ${spotX + 40},0 ${spotX + 260},880 ${spotX - 260},880`}
            fill="url(#strobeBeam)"
          />
        ))}

        {/* Suelo de calibración 3D con retícula circular */}
        <ellipse cx="960" cy="880" rx="750" ry="160" fill="none" stroke="#334155" strokeWidth="2" strokeDasharray="8 6" />
        <ellipse cx="960" cy="880" rx="480" ry="100" fill="none" stroke="#38BDF8" strokeWidth="2.5" />
        <ellipse cx="960" cy="880" rx="200" ry="45" fill="none" stroke="#FFE600" strokeWidth="2" />
      </svg>
    </div>
  );
};

/** 8. Cámara Anecoica de Pruebas Acústicas (Escena 12) */
export const CamaraAnecoicaAcusticaStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0A0D14] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Cuñas acústicas piramidales en las paredes laterales */}
        {Array.from({ length: 14 }).map((_, i) => (
          <polygon
            key={`wedge-l-${i}`}
            points={`0,${i * 65} 120,${i * 65 + 32} 0,${i * 65 + 65}`}
            fill="#1E293B"
            stroke="#000000"
            strokeWidth="3"
          />
        ))}
        {Array.from({ length: 14 }).map((_, i) => (
          <polygon
            key={`wedge-r-${i}`}
            points={`1920,${i * 65} 1800,${i * 65 + 32} 1920,${i * 65 + 65}`}
            fill="#1E293B"
            stroke="#000000"
            strokeWidth="3"
          />
        ))}

        {/* Suelo de rejilla metálica suspendida */}
        <rect x="0" y="860" width="1920" height="220" fill="#0B0F17" />
        <line x1="0" y1="860" x2="1920" y2="860" stroke="#64748B" strokeWidth="5" />

        {/* Rótulo de nivel de presión acústica SPL */}
        <g transform="translate(1480, 80)">
          <rect width="360" height="54" rx="8" fill="#000000" stroke="#10B981" strokeWidth="3" />
          <circle cx="28" cy="27" r="8" fill="#10B981" />
          <text x="50" y="34" fill="#10B981" fontSize="16" fontFamily="'Arial Black', sans-serif" fontWeight="900">
            NIVEL DE RUIDO: 0.0 dB (SILENCIO)
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 9. Hangar de Aviación al Crepúsculo (Escena 13) */
export const HangarCrepusculoStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1A0B2E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="twilightSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E1B4B" />
            <stop offset="45%" stopColor="#701A75" />
            <stop offset="75%" stopColor="#C026D3" />
            <stop offset="90%" stopColor="#EA580C" />
            <stop offset="100%" stopColor="#FBBF24" />
          </linearGradient>
        </defs>

        {/* Cielo crepuscular abierto visto a través del portón */}
        <rect x="0" y="0" width="1920" height="840" fill="url(#twilightSky)" />

        {/* Bandada de aves en formación de V cruzando el horizonte lejano */}
        <g transform="translate(1120, 240)">
          {[-60, -30, 0, 30, 60].map((bx, bi) => (
            <path
              key={`bird-${bi}`}
              d={`M ${bx} ${Math.abs(bx) * 0.6} Q ${bx + 6} ${Math.abs(bx) * 0.6 - 6} ${bx + 14} ${Math.abs(bx) * 0.6} Q ${bx + 22} ${Math.abs(bx) * 0.6 - 6} ${bx + 28} ${Math.abs(bx) * 0.6}`}
              fill="none"
              stroke="#000000"
              strokeWidth="2.5"
            />
          ))}
        </g>

        {/* Silueta de vigas maestras y dintel del portón de hangar */}
        <rect x="0" y="0" width="1920" height="90" fill="#0F172A" stroke="#000000" strokeWidth="6" />
        <rect x="0" y="0" width="140" height="860" fill="#0F172A" stroke="#000000" strokeWidth="6" />
        <rect x="1780" y="0" width="140" height="860" fill="#0F172A" stroke="#000000" strokeWidth="6" />

        {/* Suelo de hormigón del hangar */}
        <rect x="0" y="840" width="1920" height="240" fill="#1E293B" />
        <line x1="0" y1="840" x2="1920" y2="840" stroke="#000000" strokeWidth="6" />
      </svg>
    </div>
  );
};



// ===========================================================================
// ESCENARIOS CINEMÁTICOS 16:9 DEDICADOS: LA ECUACIÓN DE DRAKE
// ===========================================================================

/** 1. Tejado Suburbano Nocturno (Escenas 1 y 12) */
export const TejadoSuburbanoNocheStage: React.FC<{ frame: number }> = ({ frame }) => {
  const twinkle = (offset: number) => 0.4 + 0.6 * Math.abs(Math.sin((frame + offset) * 0.08));

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#070913] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="skyDrakeGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#05060D" />
            <stop offset="50%" stopColor="#0F172A" />
            <stop offset="80%" stopColor="#1E1B4B" />
            <stop offset="100%" stopColor="#2E1065" />
          </linearGradient>
          <radialGradient id="milkyWayBand" cx="60%" cy="30%" r="50%">
            <stop offset="0%" stopColor="rgba(216, 180, 254, 0.22)" />
            <stop offset="60%" stopColor="rgba(147, 197, 253, 0.1)" />
            <stop offset="100%" stopColor="transparent" />
          </radialGradient>
        </defs>

        {/* Firmamento nocturno profundo con banda de la Vía Láctea */}
        <rect x="0" y="0" width="1920" height="820" fill="url(#skyDrakeGrad)" />
        <ellipse cx="1150" cy="300" rx="900" ry="240" fill="url(#milkyWayBand)" transform="rotate(-18 1150 300)" />

        {/* Constelaciones y estrellas parpadeantes */}
        {Array.from({ length: 45 }).map((_, i) => {
          const sx = (i * 43 + 30) % 1920;
          const sy = (i * 29 + 20) % 640;
          const sr = (i % 3 === 0) ? 2.5 : 1.5;
          return (
            <circle
              key={`star-drake-${i}`}
              cx={sx}
              cy={sy}
              r={sr}
              fill={(i % 5 === 0) ? "#FDE047" : (i % 3 === 0 ? "#67E8F9" : "#FFFFFF")}
              opacity={twinkle(i * 12)}
            />
          );
        })}

        {/* Silueta de horizonte lejano (copas de pinos y tejados suburbanos distantes) */}
        <path
          d="M 0 780 L 120 740 L 240 760 L 380 720 L 520 750 L 680 710 L 820 740 L 1050 710 L 1220 750 L 1400 720 L 1600 760 L 1780 730 L 1920 770 L 1920 860 L 0 860 Z"
          fill="#090D16"
        />

        {/* Tejado de tejas en primer plano (tercio inferior) */}
        <polygon points="0,820 1920,780 1920,1080 0,1080" fill="#1E293B" stroke="#000000" strokeWidth="6" />
        
        {/* Filas de tejas con líneas neo-brutalistas */}
        {[860, 920, 980, 1040].map((ty, idx) => (
          <line key={`tile-${idx}`} x1="0" y1={ty} x2="1920" y2={ty - 35} stroke="#334155" strokeWidth="4" />
        ))}

        {/* Chimenea de ladrillos a la izquierda */}
        <g transform="translate(260, 680)">
          <rect width="110" height="180" fill="#7F1D1D" stroke="#000000" strokeWidth="5" />
          <rect x="-10" y="0" width="130" height="24" rx="4" fill="#991B1B" stroke="#000000" strokeWidth="5" />
          <line x1="0" y1="60" x2="110" y2="60" stroke="#000000" strokeWidth="3" />
          <line x1="0" y1="120" x2="110" y2="120" stroke="#000000" strokeWidth="3" />
        </g>

        {/* Mástil metálico de antena de televisión en el tejado */}
        <g transform="translate(420, 520)">
          <line x1="0" y1="0" x2="0" y2="280" stroke="#64748B" strokeWidth="6" />
          <line x1="-30" y1="40" x2="30" y2="40" stroke="#64748B" strokeWidth="4" />
          <line x1="-45" y1="80" x2="45" y2="80" stroke="#64748B" strokeWidth="4" />
          <circle cx="0" cy="0" r="5" fill="#EF4444" />
        </g>

        {/* Tragaluz de buhardilla iluminado con luz cálida ámbar */}
        <g transform="translate(1380, 790)">
          <polygon points="0,0 160,-20 180,80 20,100" fill="#F59E0B" stroke="#000000" strokeWidth="5" />
          <polygon points="15,10 145,-6 162,72 32,88" fill="#FDE68A" opacity="0.85" />
          <line x1="85" y1="5" x2="98" y2="80" stroke="#78350F" strokeWidth="3" />
        </g>
      </svg>
    </div>
  );
};

/** 2. Aula Histórica de Green Bank 1961 (Escena 2) */
export const AulaGreenBankStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#1C1917] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Pared con boiserie de madera de los años 60 */}
        <rect x="0" y="0" width="1920" height="780" fill="#292524" />
        {Array.from({ length: 12 }).map((_, i) => (
          <rect
            key={`panel-${i}`}
            x={i * 160 + 20}
            y="60"
            width="130"
            height="680"
            rx="4"
            fill="#3B2F2F"
            stroke="#1C1917"
            strokeWidth="4"
          />
        ))}

        {/* Cartel histórico "PROJECT OZMA - 1961" en la pared derecha */}
        <g transform="translate(1520, 140)">
          <rect width="280" height="360" rx="8" fill="#FEF3C7" stroke="#000000" strokeWidth="6" />
          <rect x="15" y="15" width="250" height="50" fill="#0F172A" />
          <text x="140" y="48" fill="#38BDF8" fontSize="22" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">PROJECT OZMA</text>
          <circle cx="140" cy="180" r="60" fill="none" stroke="#DC2626" strokeWidth="4" strokeDasharray="8 6" />
          <text x="140" y="270" fill="#1C1917" fontSize="16" fontWeight="bold" fontFamily="sans-serif" textAnchor="middle">NRAO · GREEN BANK</text>
          <text x="140" y="300" fill="#78350F" fontSize="14" fontFamily="serif" textAnchor="middle">NOVEMBER 1961</text>
        </g>

        {/* Lámparas colgantes cónicas de latón con conos de luz suave */}
        {[380, 840, 1300].map((lx, li) => (
          <g key={`lamp-${li}`} transform={`translate(${lx}, 0)`}>
            <line x1="0" y1="0" x2="0" y2="120" stroke="#000000" strokeWidth="4" />
            <polygon points="-45,160 45,160 20,120 -20,120" fill="#D97706" stroke="#000000" strokeWidth="4" />
            {/* Cono de iluminación cálida sobre el escenario */}
            <polygon points="-220,780 220,780 45,160 -45,160" fill="rgba(254, 240, 138, 0.08)" />
          </g>
        ))}

        {/* Suelo de parquet de madera noble de los años 60 */}
        <rect x="0" y="780" width="1920" height="300" fill="#451A03" stroke="#000000" strokeWidth="6" />
        <line x1="0" y1="780" x2="1920" y2="780" stroke="#000000" strokeWidth="6" />
        {[840, 910, 980, 1050].map((fy, fi) => (
          <line key={`floor-${fi}`} x1="0" y1={fy} x2="1920" y2={fy} stroke="#291205" strokeWidth="3" />
        ))}
      </svg>
    </div>
  );
};

/** 3. Panadería Cósmica en la Nebulosa R* (Escena 3) */
export const PanaderiaCosmicaNebulosaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const pulse = Math.sin(frame * 0.06) * 0.15 + 0.85;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#12041D] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="nebulaCore" cx="40%" cy="45%" r="60%">
            <stop offset="0%" stopColor="#BE185D" stopOpacity="0.65" />
            <stop offset="45%" stopColor="#831843" stopOpacity="0.45" />
            <stop offset="75%" stopColor="#3B0764" stopOpacity="0.3" />
            <stop offset="100%" stopColor="transparent" />
          </radialGradient>
        </defs>

        {/* Fondo de vacío cósmico */}
        <rect x="0" y="0" width="1920" height="1080" fill="#0C0214" />
        
        {/* Nubes moleculares masivas de hidrógeno estelar rosado */}
        <ellipse cx="680" cy="480" rx="950" ry="520" fill="url(#nebulaCore)" transform={`scale(${pulse.toFixed(3)})`} style={{ transformOrigin: "680px 480px" }} />
        
        {/* Filamentos de gas de emisión H-alfa */}
        <path
          d="M 120 200 Q 420 380 840 220 Q 1260 80 1680 320"
          stroke="#F472B6"
          strokeWidth="60"
          fill="none"
          opacity="0.25"
          filter="blur(20px)"
        />
        <path
          d="M 0 680 Q 480 520 980 720 Q 1480 920 1920 640"
          stroke="#C084FC"
          strokeWidth="80"
          fill="none"
          opacity="0.2"
          filter="blur(25px)"
        />

        {/* Estrellas jóvenes y cúmulos de protoestrellas brillantes */}
        {Array.from({ length: 30 }).map((_, i) => {
          const px = (i * 67 + 50) % 1900;
          const py = (i * 47 + 30) % 950;
          const pr = (i % 4 === 0) ? 4.5 : 2.5;
          return (
            <g key={`proto-${i}`} transform={`translate(${px}, ${py})`}>
              <circle cx="0" cy="0" r={pr * 2.2} fill="#FDE047" opacity="0.4" />
              <circle cx="0" cy="0" r={pr} fill="#FFFFFF" />
            </g>
          );
        })}

        {/* Suelo de rejilla industrial estelar en la parte inferior */}
        <rect x="0" y="940" width="1920" height="140" fill="#180728" stroke="#3B0764" strokeWidth="4" />
        <line x1="0" y1="940" x2="1920" y2="940" stroke="#F43F5E" strokeWidth="4" />
      </svg>
    </div>
  );
};

/** 4. Autopista Orbital de Exoplanetas fp (Escena 4) */
export const AutopistaOrbitalExoplanetasStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#060913] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Fondo estelar denso */}
        <rect x="0" y="0" width="1920" height="1080" fill="#04060C" />

        {/* Estrella anfitriona central en el cuadrante izquierdo */}
        <g transform="translate(360, 520)">
          <circle cx="0" cy="0" r="140" fill="#FACC15" opacity="0.2" />
          <circle cx="0" cy="0" r="85" fill="#F59E0B" stroke="#000000" strokeWidth="6" />
          <circle cx="0" cy="0" r="70" fill="#FEF08A" />
        </g>

        {/* Órbitas concéntricas elípticas de colores vibrantes estilo infografía neo-brutalista */}
        {[
          { rx: 320, ry: 160, color: "#EF4444", planetX: 280, planetR: 9, planetColor: "#F87171" },
          { rx: 540, ry: 260, color: "#10B981", planetX: -490, planetR: 14, planetColor: "#34D399" },
          { rx: 820, ry: 380, color: "#38BDF8", planetX: 740, planetR: 20, planetColor: "#60A5FA" },
          { rx: 1140, ry: 500, color: "#A855F7", planetX: -1040, planetR: 26, planetColor: "#C084FC" },
          { rx: 1480, ry: 640, color: "#F59E0B", planetX: 1360, planetR: 16, planetColor: "#FCD34D" },
        ].map((orb, idx) => (
          <g key={`orbit-${idx}`} transform="translate(360, 520)">
            <ellipse
              cx="0"
              cy="0"
              rx={orb.rx}
              ry={orb.ry}
              fill="none"
              stroke={orb.color}
              strokeWidth="4"
              strokeDasharray="16 12"
              opacity="0.8"
            />
            {/* Planeta orbitando en la elipse */}
            <circle
              cx={orb.planetX}
              cy={0}
              r={orb.planetR}
              fill={orb.planetColor}
              stroke="#000000"
              strokeWidth="4"
            />
          </g>
        ))}

        {/* Marcador métrico HUD de exoplanetas confirmados */}
        <g transform="translate(1420, 80)">
          <rect width="440" height="64" rx="8" fill="#0F172A" stroke="#10B981" strokeWidth="4" />
          <circle cx="32" cy="32" r="10" fill="#10B981" />
          <text x="58" y="40" fill="#F8FAFC" fontSize="18" fontWeight="900" fontFamily="sans-serif">
            MISIÓN KEPLER: &gt; 5,500 PLANETAS
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 5. Sistema Estelar con Diana Térmica de Ricitos de Oro ne (Escena 5) */
export const SistemaEstelarZonaHabitableStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#060814] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Estrella ardiente en el borde izquierdo */}
        <g transform="translate(-60, 540)">
          <circle cx="0" cy="0" r="320" fill="#DC2626" opacity="0.35" />
          <circle cx="0" cy="0" r="220" fill="#EA580C" stroke="#000000" strokeWidth="8" />
          <circle cx="0" cy="0" r="170" fill="#FDE047" />
        </g>

        {/* FRONTAL TÉRMICO CON TRES FRANJAS CLARAS */}
        
        {/* Zona 1: Demasiado caliente (Rojo) */}
        <rect x="220" y="0" width="460" height="1080" fill="rgba(239, 68, 68, 0.14)" />
        <line x1="680" y1="0" x2="680" y2="1080" stroke="#EF4444" strokeWidth="4" strokeDasharray="14 10" />
        <g transform="translate(450, 120)">
          <rect x="-140" y="-30" width="280" height="50" rx="6" fill="#991B1B" stroke="#000000" strokeWidth="3" />
          <text x="0" y="3" fill="#FFFFFF" fontSize="20" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">
            DEMASIADO CALIENTE
          </text>
        </g>

        {/* Zona 2: Ricitos de Oro / Zona Habitable (Verde Esmeralda) */}
        <rect x="680" y="0" width="580" height="1080" fill="rgba(16, 185, 129, 0.18)" />
        <line x1="1260" y1="0" x2="1260" y2="1080" stroke="#10B981" strokeWidth="5" />
        <g transform="translate(970, 120)">
          <rect x="-160" y="-30" width="320" height="54" rx="8" fill="#065F46" stroke="#10B981" strokeWidth="4" />
          <text x="0" y="5" fill="#A7F3D0" fontSize="22" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">
            ZONA HABITABLE (AGUA)
          </text>
        </g>

        {/* Zona 3: Demasiado fría (Azul Helado) */}
        <rect x="1260" y="0" width="660" height="1080" fill="rgba(56, 189, 248, 0.14)" />
        <g transform="translate(1580, 120)">
          <rect x="-130" y="-30" width="260" height="50" rx="6" fill="#075985" stroke="#000000" strokeWidth="3" />
          <text x="0" y="3" fill="#E0F2FE" fontSize="20" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">
            DEMASIADO FRÍO
          </text>
        </g>
      </svg>
    </div>
  );
};

/** 6. Océano Subglaciar de Europa (Escena 6) */
export const OceanoSubglaciarEuropaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const ventGlow = Math.sin(frame * 0.18) * 0.2 + 0.8;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#040817] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Capa superior: Corteza de hielo blanco-rojizo agrietada */}
        <rect x="0" y="0" width="1920" height="260" fill="#E2E8F0" stroke="#000000" strokeWidth="6" />
        <path d="M 0 240 Q 480 270 960 240 Q 1440 270 1920 240 L 1920 260 L 0 260 Z" fill="#94A3B8" />
        {/* Grietas minerales rojizas de Europa */}
        <path d="M 120 40 L 280 160 L 420 110 L 640 220" stroke="#991B1B" strokeWidth="7" fill="none" />
        <path d="M 1120 20 L 1260 140 L 1480 80 L 1640 210" stroke="#991B1B" strokeWidth="6" fill="none" />

        {/* Agujero perforado por el taladro con luz vertical */}
        <rect x="910" y="0" width="100" height="260" fill="#0F172A" stroke="#000000" strokeWidth="4" />
        <polygon points="910,260 1010,260 1140,840 780,840" fill="rgba(56, 189, 248, 0.12)" />

        {/* Océano interior líquido en penumbra abisal */}
        <rect x="0" y="260" width="1920" height="640" fill="#07132B" />
        
        {/* Fumarolas hidrotermales en el lecho rocoso (fondo) */}
        <rect x="0" y="900" width="1920" height="180" fill="#1C1917" stroke="#000000" strokeWidth="6" />
        
        {/* Chimenea volcánica hidrotermal izquierda */}
        <g transform="translate(480, 840)">
          <polygon points="-50,60 50,60 25,0 -25,0" fill="#292524" stroke="#000000" strokeWidth="4" />
          <ellipse cx="0" cy="0" rx="25" ry="8" fill="#F97316" />
          <path d="M -15 0 Q -25 -140 10 -240 Q 40 -340 0 -420" stroke="#F59E0B" strokeWidth="28" fill="none" opacity={ventGlow.toFixed(2)} filter="blur(10px)" />
        </g>

        {/* Chimenea volcánica hidrotermal derecha */}
        <g transform="translate(1440, 840)">
          <polygon points="-60,60 60,60 30,0 -30,0" fill="#292524" stroke="#000000" strokeWidth="4" />
          <ellipse cx="0" cy="0" rx="30" ry="9" fill="#EA580C" />
          <path d="M 10 0 Q 30 -160 -15 -280 Q -40 -380 10 -460" stroke="#FBBF24" strokeWidth="32" fill="none" opacity={ventGlow.toFixed(2)} filter="blur(12px)" />
        </g>
      </svg>
    </div>
  );
};

/** 7. Laboratorio de Sopa Primordial (Escena 7) */
export const LaboratorioSopaPrimordialStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Azulejos oscuros de laboratorio gótico-químico */}
        <rect x="0" y="0" width="1920" height="740" fill="#0B1329" />
        {Array.from({ length: 16 }).map((_, r) => (
          <line key={`tile-r-${r}`} x1="0" y1={r * 48} x2="1920" y2={r * 48} stroke="#1E293B" strokeWidth="1.5" />
        ))}
        {Array.from({ length: 32 }).map((_, c) => (
          <line key={`tile-c-${c}`} x1={c * 62} y1="0" x2={c * 62} y2="740" stroke="#1E293B" strokeWidth="1.5" />
        ))}

        {/* Estantería superior con frascos de reactivos químicos */}
        <rect x="180" y="240" width="680" height="16" fill="#78350F" stroke="#000000" strokeWidth="4" />
        {["CARBONO", "AMINOÁCIDOS", "FÓSFORO", "AGUA H2O"].map((txt, idx) => (
          <g key={`jar-${idx}`} transform={`translate(${230 + idx * 160}, 160)`}>
            <rect width="70" height="80" rx="8" fill="rgba(241,245,249,0.3)" stroke="#000000" strokeWidth="3.5" />
            <rect x="10" y="25" width="50" height="30" fill="#FEF3C7" stroke="#000000" strokeWidth="1.8" />
            <text x="35" y="44" fill="#000000" fontSize="8" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">{txt}</text>
          </g>
        ))}

        {/* Mesa de laboratorio de caoba maciza con encimera de pizarra */}
        <rect x="0" y="740" width="1920" height="340" fill="#3B2314" stroke="#000000" strokeWidth="6" />
        <rect x="0" y="740" width="1920" height="42" fill="#1E293B" stroke="#000000" strokeWidth="4" />
      </svg>
    </div>
  );
};

/** 8. Selva Jurásica con Asteroide Incandescente (Escena 8) */
export const SelvaJurasicaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const asteroideProgress = ((frame * 0.008) % 1.2);
  const astX = 1800 - asteroideProgress * 1400;
  const astY = -40 + asteroideProgress * 650;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B2310] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* Cielo cretácico dramático cubierto de ceniza volcánica y nubes anaranjadas */}
        <defs>
          <linearGradient id="jurassicSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#451A03" />
            <stop offset="40%" stopColor="#9A3412" />
            <stop offset="75%" stopColor="#D97706" />
            <stop offset="100%" stopColor="#14532D" />
          </linearGradient>
        </defs>
        <rect x="0" y="0" width="1920" height="680" fill="url(#jurassicSky)" />

        {/* Asteroide incandescente rasgando el firmamento con estela de fuego */}
        <g transform={`translate(${astX.toFixed(1)}, ${astY.toFixed(1)})`}>
          {/* Estela masiva de humo y fuego */}
          <line x1="0" y1="0" x2="420" y2="-190" stroke="#F59E0B" strokeWidth="24" strokeLinecap="round" opacity="0.8" />
          <line x1="0" y1="0" x2="380" y2="-170" stroke="#EF4444" strokeWidth="14" strokeLinecap="round" />
          <line x1="0" y1="0" x2="260" y2="-115" stroke="#FEF08A" strokeWidth="8" strokeLinecap="round" />
          {/* Núcleo ardiente de roca espacial */}
          <circle cx="0" cy="0" r="32" fill="#FACC15" stroke="#DC2626" strokeWidth="6" />
          <circle cx="0" cy="0" r="20" fill="#FFFFFF" />
        </g>

        {/* Volcán cónico humeante en el horizonte lejano */}
        <polygon points="1200,680 1380,360 1560,680" fill="#1C1917" stroke="#000000" strokeWidth="6" />
        <ellipse cx="1380" cy="360" rx="30" ry="10" fill="#EA580C" />
        <path d="M 1380 350 Q 1420 220 1360 120" stroke="#78350F" strokeWidth="38" fill="none" opacity="0.6" filter="blur(8px)" />

        {/* Fronda jurásica: Helechos gigantes y cicadáceas */}
        <rect x="0" y="680" width="1920" height="400" fill="#052E16" stroke="#000000" strokeWidth="6" />
        
        {/* Troncos y hojas masivas en los bordes de la pantalla */}
        {[-40, 160, 1720, 1860].map((tx, ti) => (
          <g key={`tree-${ti}`} transform={`translate(${tx}, 440)`}>
            <rect width="60" height="340" fill="#1C1917" stroke="#000000" strokeWidth="5" />
            <path d="M -80 0 Q 30 -140 140 0" fill="#15803D" stroke="#000000" strokeWidth="4" />
            <path d="M -110 40 Q 30 -90 170 40" fill="#166534" stroke="#000000" strokeWidth="4" />
          </g>
        ))}
      </svg>
    </div>
  );
};

/** 9. Fondo Oceánico y Superficie Marina (Escena 9) */
export const FondoOceanicoFilosofosStage: React.FC<{ frame: number }> = ({ frame }) => {
  const waveOffset = Math.sin(frame * 0.08) * 12;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#022C43] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* MITAD SUPERIOR: Cielo nublado y superficie del mar (y: 0 a 280) */}
        <rect x="0" y="0" width="1920" height="280" fill="#64748B" />
        
        {/* Balsa de rescate del Stickman flotando en la superficie */}
        <g transform={`translate(960, ${270 + waveOffset.toFixed(1)})`}>
          <rect x="-80" y="-12" width="160" height="24" rx="10" fill="#78350F" stroke="#000000" strokeWidth="4" />
          <line x1="-50" y1="-12" x2="-50" y2="12" stroke="#451A03" strokeWidth="3" />
          <line x1="50" y1="-12" x2="50" y2="12" stroke="#451A03" strokeWidth="3" />
        </g>

        {/* Línea de oleaje en la superficie marina */}
        <path
          d={`M 0 280 Q 480 ${260 + waveOffset} 960 280 Q 1440 ${300 - waveOffset} 1920 280 L 1920 1080 L 0 1080 Z`}
          fill="#0C4A6E"
        />

        {/* MITAD INFERIOR: Aguas profundas azul turquesa y abisal */}
        <rect x="0" y="320" width="1920" height="760" fill="#082F49" />

        {/* Rayos de luz solar penetrando en el agua (cáusticas subacuáticas) */}
        {[240, 580, 1020, 1420].map((rx, ri) => (
          <polygon
            key={`ray-${ri}`}
            points={`${rx},280 ${rx + 120},280 ${rx + 280},960 ${rx + 40},960`}
            fill="rgba(56, 189, 248, 0.09)"
          />
        ))}

        {/* Fondo marino arenoso con corales y conchas */}
        <rect x="0" y="920" width="1920" height="160" fill="#042F2E" stroke="#000000" strokeWidth="6" />
        <path d="M 0 920 Q 480 890 960 920 Q 1440 940 1920 910 L 1920 1080 L 0 1080 Z" fill="#134E4A" />

        {/* Algas marinas ondulantes en los laterales */}
        {[140, 220, 1680, 1780].map((kx, ki) => (
          <path
            key={`kelp-${ki}`}
            d={`M ${kx} 940 Q ${kx + Math.sin(frame * 0.1 + ki) * 35} 740 ${kx} 580`}
            stroke="#10B981"
            strokeWidth="14"
            strokeLinecap="round"
            fill="none"
          />
        ))}
      </svg>
    </div>
  );
};

/** 10. Casino Estelar y Vista Cenital de la Vía Láctea L (Escena 10) */
export const CasinoEstelarDrakeStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#05060D] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <radialGradient id="mwSpiral" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#FDE047" stopOpacity="0.9" />
            <stop offset="20%" stopColor="#C084FC" stopOpacity="0.5" />
            <stop offset="55%" stopColor="#38BDF8" stopOpacity="0.25" />
            <stop offset="100%" stopColor="transparent" />
          </radialGradient>
        </defs>

        {/* Vista cenital completa del disco galáctico de la Vía Láctea */}
        <g transform="translate(960, 540)">
          <ellipse cx="0" cy="0" rx="840" ry="460" fill="url(#mwSpiral)" />
          {/* Brazos espirales */}
          <path
            d="M 0 0 C 220 -80, 480 -220, 720 -80"
            stroke="#E9D5FF"
            strokeWidth="48"
            fill="none"
            opacity="0.3"
            filter="blur(18px)"
          />
          <path
            d="M 0 0 C -220 80, -480 220, -720 80"
            stroke="#BAE6FD"
            strokeWidth="48"
            fill="none"
            opacity="0.3"
            filter="blur(18px)"
          />

          {/* Civilizaciones que se encienden como cerillas y se apagan en ceniza gris */}
          {[
            { x: -320, y: -120, born: 10, dur: 70 },
            { x: 240, y: -180, born: 45, dur: 60 },
            { x: -140, y: 160, born: 80, dur: 65 },
            { x: 420, y: 140, born: 120, dur: 55 },
            { x: -540, y: -40, born: 160, dur: 75 },
            { x: 180, y: 80, born: 200, dur: 60 },
          ].map((civ, ci) => {
            const age = (frame - civ.born) % 240;
            const isAlive = age >= 0 && age < civ.dur;
            const glow = isAlive ? Math.sin((age / civ.dur) * Math.PI) : 0;
            return (
              <g key={`civ-${ci}`} transform={`translate(${civ.x}, ${civ.y})`}>
                {isAlive ? (
                  <>
                    <circle cx="0" cy="0" r={16 * glow} fill="#38BDF8" opacity="0.4" />
                    <circle cx="0" cy="0" r={4} fill="#FFFFFF" />
                    {/* Ondas concéntricas de radio */}
                    <circle cx="0" cy="0" r={8 + age * 1.5} fill="none" stroke="#38BDF8" strokeWidth="2" opacity={Math.max(0, 1 - (age / civ.dur))} />
                  </>
                ) : (
                  <circle cx="0" cy="0" r="2.5" fill="#475569" opacity="0.4" />
                )}
              </g>
            );
          })}
        </g>
      </svg>
    </div>
  );
};

/** 11. Umbral Dividido del Gran Filtro (Escena 11) */
export const UmbralGranFiltroStage: React.FC<{ frame: number }> = ({ frame }) => {
  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#090D16] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* LADO IZQUIERDO: Universo Pesimista y Desértico (N = 1, Soledad) */}
        <rect x="0" y="0" width="960" height="1080" fill="#0B132B" />
        <g transform="translate(420, 520)">
          {/* Campana de cristal sobre la solitaria Tierra */}
          <path d="M -90 120 L -90 0 C -90 -100 90 -100 90 0 L 90 120 Z" fill="rgba(56, 189, 248, 0.08)" stroke="#38BDF8" strokeWidth="5" />
          <circle cx="0" cy="40" r="48" fill="#0284C7" stroke="#000000" strokeWidth="5" />
          <text x="0" y="170" fill="#93C5FD" fontSize="28" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">N = 1 (ESTAMOS SOLOS)</text>
        </g>

        {/* LADO DERECHO: Universo Optimista (Esferas de Dyson, Megaciudades) */}
        <rect x="960" y="0" width="960" height="1080" fill="#2E0854" />
        <g transform="translate(1500, 520)">
          {/* Enjambre y Esfera de Dyson dorada alrededor de su estrella */}
          <circle cx="0" cy="0" r="160" fill="none" stroke="#FDE047" strokeWidth="8" strokeDasharray="24 16" />
          <circle cx="0" cy="0" r="220" fill="none" stroke="#F59E0B" strokeWidth="5" strokeDasharray="36 20" />
          <circle cx="0" cy="0" r="48" fill="#FACC15" stroke="#000000" strokeWidth="5" />
          {/* Rayos de luz y autopistas cósmicas */}
          <line x1="-180" y1="-180" x2="180" y2="180" stroke="#EC4899" strokeWidth="4" />
          <line x1="-180" y1="180" x2="180" y2="-180" stroke="#EC4899" strokeWidth="4" />
          <text x="0" y="270" fill="#FDE047" fontSize="28" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">N = 50,000 (MEGACIVILIZACIONES)</text>
        </g>

        {/* MURO CENTRAL DEL GRAN FILTRO: Titánico monolito divisorio */}
        <rect x="930" y="0" width="60" height="1080" fill="#000000" stroke="#EF4444" strokeWidth="4" />
        <line x1="960" y1="0" x2="960" y2="1080" stroke="#DC2626" strokeWidth="8" strokeDasharray="30 18" />
      </svg>
    </div>
  );
};


/* ============================================================================
 * ESCENARIOS EXCLUSIVOS 16:9 — EPISODIO: "LA TRAMPA DEL CEREBRO"
 * ============================================================================ */

/** 1. Galería de Museo de Historia Natural con transición orgánica al Arbusto Filogenético */
export const GaleriaMuseoEvolucionStage: React.FC<{ frame: number }> = ({ frame }) => {
  // Pasado el ecuador de la escena (~560 frames), las paredes se atenúan revelando el arbusto filogenético vivo
  const bushPhase = Math.max(0, Math.min(1, (frame - 540) / 75));
  const spotlightPulse = 0.85 + Math.sin(frame * 0.12) * 0.1;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B0F19] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="museumWall" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E293B" />
            <stop offset="100%" stopColor="#0F172A" />
          </linearGradient>
          <linearGradient id="parquetFloor" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#78350F" />
            <stop offset="100%" stopColor="#3B1806" />
          </linearGradient>
          <radialGradient id="museumSpot" cx="0.5" cy="0" r="0.85">
            <stop offset="0%" stopColor="#FEF08A" stopOpacity={0.34 * spotlightPulse} />
            <stop offset="55%" stopColor="#F59E0B" stopOpacity={0.11 * spotlightPulse} />
            <stop offset="100%" stopColor="#0F172A" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Pared de galería clásica */}
        <rect x="0" y="0" width="1920" height="780" fill="url(#museumWall)" opacity={1 - bushPhase * 0.72} />

        {/* Columnas neoclásicas laterales del museo */}
        {[-1, 1].map((side, idx) => {
          const cx = side === -1 ? 110 : 1810;
          return (
            <g key={`col-${idx}`} opacity={1 - bushPhase * 0.65}>
              <rect x={cx - 52} y="60" width="104" height="720" fill="#334155" stroke="#000000" strokeWidth="6" />
              <line x1={cx - 22} y1="80" x2={cx - 22} y2="760" stroke="#1E293B" strokeWidth="5" />
              <line x1={cx + 22} y1="80" x2={cx + 22} y2="760" stroke="#1E293B" strokeWidth="5" />
              <rect x={cx - 68} y="40" width="136" height="32" rx="4" fill="#475569" stroke="#000000" strokeWidth="5" />
              <rect x={cx - 68} y="752" width="136" height="30" rx="4" fill="#475569" stroke="#000000" strokeWidth="5" />
            </g>
          );
        })}

        {/* Zócalo y moldura dorada */}
        <rect x="0" y="742" width="1920" height="38" fill="#0F172A" stroke="#000000" strokeWidth="5" opacity={1 - bushPhase * 0.5} />
        <line x1="0" y1="748" x2="1920" y2="748" stroke="#D97706" strokeWidth="3" opacity={1 - bushPhase * 0.5} />

        {/* Focos cenitales de galería */}
        <polygon points="960,0 420,780 1500,780" fill="url(#museumSpot)" />
        <rect x="880" y="16" width="160" height="24" rx="6" fill="#000000" stroke="#F59E0B" strokeWidth="3" />

        {/* Fibras bioluminiscentes del Árbol/Arbusto Filogenético Real emergiendo en el fondo */}
        {bushPhase > 0.02 && (
          <g opacity={bushPhase} transform="translate(960, 460)">
            {[
              "M 0 280 C -180 120, -480 40, -760 -190",
              "M 0 280 C -120 40, -320 -150, -540 -330",
              "M 0 280 C -40 20, -140 -220, -190 -380",
              "M 0 280 C 60 30, 180 -190, 240 -370",
              "M 0 280 C 170 80, 440 -120, 660 -310",
              "M 0 280 C 260 150, 560 10, 820 -140",
              "M -310 -40 C -450 -140, -640 -90, -820 -260",
              "M 290 -30 C 440 -160, 620 -210, 810 -280",
            ].map((d, i) => (
              <path
                key={`phy-${i}`}
                d={d}
                fill="none"
                stroke={i % 2 === 0 ? "#10B981" : "#34D399"}
                strokeWidth={5 - (i % 2)}
                strokeDasharray="16 8"
                opacity={0.55 + Math.sin(frame * 0.14 + i) * 0.2}
              />
            ))}
            {/* Nodos de reinos biológicos en el fondo */}
            {[
              { x: -740, y: -185, label: "BACTERIA" },
              { x: -520, y: -315, label: "ARCHAEA" },
              { x: 235, y: -355, label: "FUNGI" },
              { x: 645, y: -295, label: "PLANTAE" },
              { x: 800, y: -135, label: "ARTHROPODA" },
            ].map((n, idx) => (
              <g key={`knode-${idx}`} transform={`translate(${n.x}, ${n.y})`}>
                <circle cx="0" cy="0" r="10" fill="#10B981" stroke="#000000" strokeWidth="3" />
                <text x="0" y="-18" textAnchor="middle" fill="#A7F3D0" fontSize="15" fontWeight="900" fontFamily="sans-serif">
                  {n.label}
                </text>
              </g>
            ))}
          </g>
        )}

        {/* Suelo de parquet encerado con líneas de perspectiva */}
        <rect x="0" y="780" width="1920" height="300" fill="url(#parquetFloor)" stroke="#000000" strokeWidth="6" opacity={1 - bushPhase * 0.35} />
        {[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5].map((i) => (
          <line
            key={`pq-${i}`}
            x1={960 + i * 145}
            y1="780"
            x2={960 + i * 290}
            y2="1080"
            stroke="#291003"
            strokeWidth="3.5"
            opacity={0.75}
          />
        ))}

        {/* Catenarias de terciopelo rojo en los extremos del museo */}
        {[-680, 680].map((bx, i) => (
          <g key={`velvet-${i}`} transform={`translate(${960 + bx}, 795)`} opacity={1 - bushPhase * 0.75}>
            <rect x="-18" y="65" width="36" height="12" rx="4" fill="#F59E0B" stroke="#000000" strokeWidth="4" />
            <line x1="0" y1="0" x2="0" y2="65" stroke="#FACC15" strokeWidth="8" />
            <circle cx="0" cy="0" r="10" fill="#FDE047" stroke="#000000" strokeWidth="3.5" />
          </g>
        ))}
      </svg>
    </div>
  );
};

/** 2. Estadio Olímpico de Biomasa Planetaria */
export const EstadioPodioBiomasaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const barGrow = Math.min(1, Math.max(0.25, frame / 90));
  const confettiFloat = Math.sin(frame * 0.14) * 8;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#E0F2FE] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="stadiumSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#BAE6FD" />
            <stop offset="100%" stopColor="#F0F9FF" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="1920" height="790" fill="url(#stadiumSky)" />

        {/* Barras monumentales de Biomasa Global de Carbono (Gt C) a izquierda y derecha */}
        <g transform="translate(115, 780)">
          <rect x="0" y={-520 * barGrow} width="115" height={520 * barGrow} rx="8" fill="#10B981" stroke="#000000" strokeWidth="5" />
          <text x="57" y={-520 * barGrow - 16} textAnchor="middle" fill="#065F46" fontSize="20" fontWeight="900">PLANTAS 82%</text>

          <rect x="135" y={-360 * barGrow} width="115" height={360 * barGrow} rx="8" fill="#F59E0B" stroke="#000000" strokeWidth="5" />
          <text x="192" y={-360 * barGrow - 16} textAnchor="middle" fill="#92400E" fontSize="20" fontWeight="900">BACTERIAS 13%</text>
        </g>

        <g transform="translate(1540, 780)">
          <rect x="0" y={-230 * barGrow} width="115" height={230 * barGrow} rx="8" fill="#0284C7" stroke="#000000" strokeWidth="5" />
          <text x="57" y={-230 * barGrow - 16} textAnchor="middle" fill="#075985" fontSize="19" fontWeight="900">ARTRÓPODOS</text>

          <rect x="135" y={-14} width="115" height="14" rx="4" fill="#EF4444" stroke="#000000" strokeWidth="4" />
          <text x="192" y="-26" textAnchor="middle" fill="#B91C1C" fontSize="19" fontWeight="900">HUMANOS 0.01%</text>
        </g>

        {/* Banderines olímpicos evolutivos superiores */}
        <path d="M 0 110 Q 480 175 960 115 Q 1440 175 1920 110" fill="none" stroke="#000000" strokeWidth="5" />
        {Array.from({ length: 16 }).map((_, i) => (
          <polygon
            key={`flag-${i}`}
            points={`${90 + i * 115},${122 + (i % 2) * 14} ${118 + i * 115},${164 + confettiFloat * 0.3} ${146 + i * 115},${122 + (i % 2) * 14}`}
            fill={i % 3 === 0 ? "#FFE600" : i % 3 === 1 ? "#10B981" : "#F97316"}
            stroke="#000000"
            strokeWidth="3.5"
          />
        ))}

        {/* Pista atlética de tartán rojo neo-brutalista */}
        <rect x="0" y="785" width="1920" height="295" fill="#DC2626" stroke="#000000" strokeWidth="6" />
        <line x1="0" y1="845" x2="1920" y2="845" stroke="#FFFFFF" strokeWidth="5" strokeDasharray="36 18" />
        <line x1="0" y1="925" x2="1920" y2="925" stroke="#FFFFFF" strokeWidth="5" strokeDasharray="48 22" />
      </svg>
    </div>
  );
};

/** 3. Pantalla Dividida: Estación Clínica de Rayos X Metabólicos (Izquierda) vs Sabana Árida (Derecha) */
export const SabanaMetabolicaSplitStage: React.FC<{ frame: number }> = ({ frame }) => {
  const heatShimmer = Math.sin(frame * 0.15) * 6;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0F172A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* IZQUIERDA: Cabina de Diagnóstico Metabólico en Rayos X */}
        <rect x="0" y="0" width="960" height="790" fill="#0B132B" />
        {Array.from({ length: 10 }).map((_, i) => (
          <line key={`gx-${i}`} x1={i * 96} y1="0" x2={i * 96} y2="790" stroke="#1E293B" strokeWidth="2" />
        ))}
        {Array.from({ length: 8 }).map((_, i) => (
          <line key={`gy-${i}`} x1="0" y1={i * 100} x2="960" y2={i * 100} stroke="#1E293B" strokeWidth="2" />
        ))}
        <rect x="0" y="790" width="960" height="290" fill="#1E293B" stroke="#000000" strokeWidth="6" />

        {/* DERECHA: Sabana Africana bajo Sequía Abrasadora */}
        <rect x="960" y="0" width="960" height="790" fill="#FEF3C7" />
        <circle cx="1710" cy={195 + heatShimmer * 0.4} r="88" fill="#F97316" stroke="#000000" strokeWidth="5" />
        <circle cx="1710" cy={195 + heatShimmer * 0.4} r="118" fill="#FB923C" opacity="0.24" />
        {/* Silueta lejana de acacia y colina seca */}
        <path d="M 960 790 Q 1240 725 1540 765 Q 1760 735 1920 790 Z" fill="#D97706" stroke="#000000" strokeWidth="4" />
        <g transform="translate(1760, 755)">
          <path d="M -8 0 L -4 -95 L -55 -130 M 4 -95 L 62 -128" stroke="#451A03" strokeWidth="9" fill="none" strokeLinecap="round" />
          <ellipse cx="0" cy="-136" rx="105" ry="22" fill="#65A30D" stroke="#000000" strokeWidth="4" />
        </g>
        <rect x="960" y="790" width="960" height="290" fill="#F59E0B" stroke="#000000" strokeWidth="6" />

        {/* Divisor central neo-brutalista */}
        <rect x="952" y="0" width="16" height="1080" fill="#000000" />
        <line x1="960" y1="0" x2="960" y2="1080" stroke="#FFE600" strokeWidth="4" strokeDasharray="20 14" />
      </svg>
    </div>
  );
};

/** 4. Pantalla Dividida: Bosque Húmedo de Montaña (Gorila) vs Campamento Paleolítico con Fuego */
export const BosqueGorilaCampamentoFuegoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const fireGlow = 0.82 + Math.sin(frame * 0.2) * 0.15;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#091510] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* IZQUIERDA: Selva húmeda de montaña */}
        <rect x="0" y="0" width="960" height="790" fill="#064E3B" />
        {[120, 340, 780].map((tx, idx) => (
          <g key={`trunk-${idx}`}>
            <rect x={tx} y="0" width="76" height="790" fill="#022C22" stroke="#000000" strokeWidth="5" />
            <ellipse cx={tx + 38} cy="110" rx="150" ry="70" fill="#047857" stroke="#000000" strokeWidth="4" />
          </g>
        ))}
        <rect x="0" y="790" width="960" height="290" fill="#14532D" stroke="#000000" strokeWidth="6" />

        {/* DERECHA: Campamento Paleolítico al Crepúsculo */}
        <rect x="960" y="0" width="960" height="790" fill="#1E1B4B" />
        {/* Resplandor cálido de fogata paleolítica */}
        <circle cx="1440" cy="720" r={360 * fireGlow} fill="#F97316" opacity="0.22" />
        <circle cx="1440" cy="740" r={210 * fireGlow} fill="#FACC15" opacity="0.18" />
        {/* Abrigo rocoso paleolítico al fondo */}
        <polygon points="1540,790 1690,410 1920,340 1920,790" fill="#334155" stroke="#000000" strokeWidth="6" />
        <rect x="960" y="790" width="960" height="290" fill="#451A03" stroke="#000000" strokeWidth="6" />

        {/* Divisor central */}
        <rect x="952" y="0" width="16" height="1080" fill="#000000" />
      </svg>
    </div>
  );
};

/** 5. Laboratorio Anatómico de Biomecánica Obstétrica */
export const LaboratorioBiomecanicaPelvisStage: React.FC<{ frame: number }> = ({ frame }) => {
  const scanY = 120 + ((frame * 2.2) % 580);

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#111827] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <rect x="0" y="0" width="1920" height="790" fill="#111827" />
        {/* Retícula métrica cian sutil */}
        {Array.from({ length: 20 }).map((_, i) => (
          <line key={`bmx-${i}`} x1={i * 100} y1="0" x2={i * 100} y2="790" stroke="#1F2937" strokeWidth="2" />
        ))}
        {Array.from({ length: 9 }).map((_, i) => (
          <line key={`bmy-${i}`} x1="0" y1={i * 95} x2="1920" y2={i * 95} stroke="#1F2937" strokeWidth="2" />
        ))}
        {/* Línea horizontal de escaneo láser anatómico */}
        <line x1="140" y1={scanY} x2="1780" y2={scanY} stroke="#22D3EE" strokeWidth="2" opacity="0.25" />

        {/* Lámpara quirúrgica cenital */}
        <g transform="translate(960, 42)">
          <rect x="-150" y="-22" width="300" height="36" rx="12" fill="#334155" stroke="#000000" strokeWidth="5" />
          <polygon points="-140,14 -520,790 520,790 140,14" fill="#38BDF8" opacity="0.07" />
        </g>

        {/* Piso clínico grafito */}
        <rect x="0" y="790" width="1920" height="290" fill="#1E293B" stroke="#000000" strokeWidth="6" />
        <line x1="0" y1="802" x2="1920" y2="802" stroke="#38BDF8" strokeWidth="3" opacity="0.55" />
      </svg>
    </div>
  );
};

/** 6. Pantalla Dividida: Pradera Soleada de Cebras (20 min) vs Refugio Tribal Cooperativo (1 año) */
export const PraderaCebraRefugioTribalStage: React.FC<{ frame: number }> = ({ frame }) => {
  const cloudDrift = Math.sin(frame * 0.08) * 18;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#FEF9C3] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* IZQUIERDA: Pradera abierta soleada */}
        <rect x="0" y="0" width="960" height="790" fill="#BAE6FD" />
        <circle cx="170" cy="180" r="62" fill="#FACC15" stroke="#000000" strokeWidth="5" />
        <ellipse cx={520 + cloudDrift} cy="190" rx="110" ry="36" fill="#FFFFFF" stroke="#000000" strokeWidth="4" />
        <path d="M 0 790 Q 320 710 640 755 Q 820 730 960 790 Z" fill="#84CC16" stroke="#000000" strokeWidth="4" />
        <rect x="0" y="790" width="960" height="290" fill="#65A30D" stroke="#000000" strokeWidth="6" />

        {/* Rótulo superior izquierdo */}
        <g transform="translate(480, 212)">
          <rect x="-340" y="-28" width="680" height="54" rx="12" fill="#10B981" stroke="#000000" strokeWidth="5" />
          <text x="0" y="7" textAnchor="middle" fill="#000000" fontSize="22" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            CEBRA EN LA SABANA (TRAS NACER: 15-20 MIN)
          </text>
        </g>

        {/* DERECHA: Refugio tribal resguardado */}
        <rect x="960" y="0" width="960" height="790" fill="#292524" />
        <path d="M 960 220 Q 1440 80 1920 260 L 1920 790 L 960 790 Z" fill="#44403C" stroke="#000000" strokeWidth="6" />
        <circle cx="1440" cy="730" r="260" fill="#F59E0B" opacity="0.16" />
        <rect x="960" y="790" width="960" height="290" fill="#57534E" stroke="#000000" strokeWidth="6" />

        {/* Rótulo superior derecho */}
        <g transform="translate(1440, 212)">
          <rect x="-340" y="-28" width="680" height="54" rx="12" fill="#F97316" stroke="#000000" strokeWidth="5" />
          <text x="0" y="7" textAnchor="middle" fill="#000000" fontSize="22" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            BEBÉ HUMANO (TRAS NACER: 1 AÑO + TRIBU)
          </text>
        </g>

        <rect x="952" y="0" width="16" height="1080" fill="#000000" />
      </svg>
    </div>
  );
};

/** 7. Arrecife de Coral Subacuático (Pulpo Común) */
export const ArrecifeCoralSubmarinoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const waveShift = Math.sin(frame * 0.12) * 20;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#042F2E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="reefWater" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#0891B2" />
            <stop offset="55%" stopColor="#0F766E" />
            <stop offset="100%" stopColor="#042F2E" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="1920" height="800" fill="url(#reefWater)" />

        {/* Rayos cáusticos refractados desde las olas de la superficie */}
        {[260, 680, 1180, 1620].map((rx, i) => (
          <polygon
            key={`caustic-${i}`}
            points={`${rx + waveShift * 0.5},0 ${rx - 140},800 ${rx + 110},800 ${rx + 70 + waveShift * 0.5},0`}
            fill="#67E8F9"
            opacity="0.11"
          />
        ))}

        {/* Formaciones de coral y algas marinas suaves */}
        {[180, 1720].map((cx, i) => {
          const sway = Math.sin(frame * 0.14 + i) * 12;
          return (
            <g key={`coral-${i}`} transform={`translate(${cx}, 800)`}>
              <path
                d={`M 0 0 C -30 -90, ${-50 + sway} -180, ${-20 + sway} -260`}
                fill="none"
                stroke="#F43F5E"
                strokeWidth="26"
                strokeLinecap="round"
              />
              <path
                d={`M 30 0 C 60 -80, ${75 + sway} -150, ${45 + sway} -220`}
                fill="none"
                stroke="#FB923C"
                strokeWidth="22"
                strokeLinecap="round"
              />
            </g>
          );
        })}

        {/* Burbujas ascendentes suaves */}
        {Array.from({ length: 14 }).map((_, i) => {
          const bx = (i * 142 + 70) % 1860;
          const by = 800 - ((frame * 1.8 + i * 65) % 780);
          return (
            <circle key={`bub-${i}`} cx={bx} cy={by} r={5 + (i % 3) * 3} fill="none" stroke="#A5F3FC" strokeWidth="2.5" opacity="0.6" />
          );
        })}

        {/* Lecho arenoso marino */}
        <rect x="0" y="800" width="1920" height="280" fill="#134E4A" stroke="#000000" strokeWidth="6" />
        <path d="M 0 835 Q 480 815 960 838 Q 1440 858 1920 832" fill="none" stroke="#2DD4BF" strokeWidth="3" opacity="0.4" />
      </svg>
    </div>
  );
};

/** 8. Pantalla Dividida: Fondo Marino sin Fuego (Delfín) vs Parque Aéreo (Cuervo y Gravedad) */
export const OceanoVsParqueAereoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const leafSway = Math.sin(frame * 0.13) * 6;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0C4A6E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        {/* IZQUIERDA: Medio Marino Hidrodinámico */}
        <rect x="0" y="0" width="960" height="790" fill="#0369A1" />
        <path d="M 0 85 Q 240 60 480 85 Q 720 110 960 85" fill="none" stroke="#7DD3FC" strokeWidth="5" />
        <rect x="0" y="790" width="960" height="290" fill="#082F49" stroke="#000000" strokeWidth="6" />
        <g transform="translate(480, 145)">
          <rect x="-310" y="-26" width="620" height="50" rx="10" fill="#0284C7" stroke="#000000" strokeWidth="5" />
          <text x="0" y="7" textAnchor="middle" fill="#FFFFFF" fontSize="21" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            OCÉANO: ALETAS + CERO FUEGO SUBMARINO
          </text>
        </g>

        {/* DERECHA: Aire y Rama de Parque (Física del Vuelo) */}
        <rect x="960" y="0" width="960" height="790" fill="#E0F2FE" />
        {/* Tronco y rama robusta de roble */}
        <rect x="1790" y="180" width="130" height="610" fill="#78350F" stroke="#000000" strokeWidth="6" />
        <path
          d={`M 1800 410 Q 1520 ${395 + leafSway} 1270 ${425 + leafSway}`}
          fill="none"
          stroke="#78350F"
          strokeWidth="34"
          strokeLinecap="round"
        />
        <ellipse cx="1760" cy="180" rx="220" ry="110" fill="#16A34A" stroke="#000000" strokeWidth="5" />
        <rect x="960" y="790" width="960" height="290" fill="#4ADE80" stroke="#000000" strokeWidth="6" />
        <g transform="translate(1440, 145)">
          <rect x="-310" y="-26" width="620" height="50" rx="10" fill="#FFE600" stroke="#000000" strokeWidth="5" />
          <text x="0" y="7" textAnchor="middle" fill="#000000" fontSize="21" fontWeight="900" fontFamily="'Arial Black', sans-serif">
            AIRE: LÍMITE ESTRICTO DE PESO CRANEAL
          </text>
        </g>

        <rect x="952" y="0" width="16" height="1080" fill="#000000" />
      </svg>
    </div>
  );
};

/** 9. Taller Lítico Paleolítico Flanqueado por Proyección Holográfica de la Corteza Motora */
export const TallerLiticoCortezaMotoraStage: React.FC<{ frame: number }> = ({ frame }) => {
  const synapseGlow = 0.45 + Math.abs(Math.sin(frame * 0.18)) * 0.5;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#0B101E] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <rect x="0" y="0" width="1920" height="790" fill="#0B101E" />

        {/* Proyecciones holográficas gigantes de los hemisferios cerebrales y la Corteza Motora (M1) a ambos lados */}
        {[-1, 1].map((side, idx) => (
          <g
            key={`lobe-${idx}`}
            transform={`translate(${side === -1 ? 310 : 1610}, 390) scale(${side}, 1)`}
          >
            <path
              d="M -210 110 C -240 -60, -130 -210, 40 -200 C 190 -190, 250 -50, 210 110 C 120 165, -110 165, -210 110 Z"
              fill="#0F172A"
              stroke="#38BDF8"
              strokeWidth="5"
            />
            {/* Franja de la Corteza Motora Primaria y Premotora encendiéndose */}
            <path
              d="M -30 -195 C 10 -90, 5 30, -20 140 C 35 140, 60 25, 45 -188 Z"
              fill="#FFE600"
              opacity={synapseGlow}
              stroke="#F97316"
              strokeWidth="3"
            />
            {/* Red sináptica */}
            {[
              [-110, -70, -10, -95],
              [-10, -95, 110, -40],
              [-80, 35, 15, 10],
              [15, 10, 125, 55],
            ].map(([x1, y1, x2, y2], k) => (
              <line key={k} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#22D3EE" strokeWidth="3" strokeDasharray="8 5" />
            ))}
          </g>
        ))}

        {/* Suelo de taller lítico con lascas de sílex esparcidas */}
        <rect x="0" y="790" width="1920" height="290" fill="#3F2E21" stroke="#000000" strokeWidth="6" />
        {[240, 520, 820, 1140, 1460, 1690].map((fx, i) => (
          <polygon
            key={`flake-${i}`}
            points={`${fx},835 ${fx + 28},822 ${fx + 44},844 ${fx + 14},852`}
            fill="#64748B"
            stroke="#000000"
            strokeWidth="3"
          />
        ))}
      </svg>
    </div>
  );
};

/** 10. Gran Valle del Rift del Pleistoceno (Montaña Rusa Climática: Selva -> Sequía -> Lago) */
export const ValleRiftPleistocenoStage: React.FC<{ frame: number }> = ({ frame }) => {
  // Ciclo climático suave a lo largo de la escena (0: húmedo verde, 1: sequía árida, 2: lago intermitente)
  const cycle = (frame % 360) / 360;
  const isDrought = cycle >= 0.33 && cycle < 0.68;
  const isLake = cycle >= 0.68;

  const skyColor = isDrought ? "#FDE68A" : isLake ? "#BAE6FD" : "#A7F3D0";
  const groundColor = isDrought ? "#D97706" : isLake ? "#65A30D" : "#15803D";
  const hillColor = isDrought ? "#B45309" : "#166534";
  const dustX = (frame * 6) % 1920;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 overflow-hidden" style={{ backgroundColor: skyColor }}>
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <rect x="0" y="0" width="1920" height="790" fill={skyColor} />

        {/* Sol abrasador o nubes de monzón según fase climática */}
        {isDrought ? (
          <circle cx="1580" cy="185" r="92" fill="#EF4444" stroke="#000000" strokeWidth="5" />
        ) : (
          <g>
            <circle cx="1580" cy="185" r="70" fill="#FACC15" stroke="#000000" strokeWidth="5" />
            <ellipse cx="460" cy="175" rx="165" ry="52" fill="#FFFFFF" stroke="#000000" strokeWidth="4" />
            <ellipse cx="1160" cy="155" rx="145" ry="46" fill="#F8FAFC" stroke="#000000" strokeWidth="4" />
          </g>
        )}

        {/* Escarpes tectónicos del Gran Valle del Rift */}
        <polygon points="0,790 280,470 640,620 1060,450 1480,610 1920,460 1920,790" fill={hillColor} stroke="#000000" strokeWidth="5" opacity="0.85" />

        {/* Lago efímero del Rift cuando entra la fase lacustre */}
        {isLake && (
          <ellipse cx="1360" cy="790" rx="460" ry="55" fill="#0284C7" stroke="#000000" strokeWidth="5" />
        )}

        {/* Remolinos de polvo en fase de sequía */}
        {isDrought && (
          <path
            d={`M ${dustX} 760 Q ${dustX + 40} 650 ${dustX - 20} 540 Q ${dustX + 60} 440 ${dustX + 10} 350`}
            fill="none"
            stroke="#92400E"
            strokeWidth="12"
            strokeDasharray="18 12"
            opacity="0.55"
          />
        )}

        {/* Suelo del Valle del Rift */}
        <rect x="0" y="790" width="1920" height="290" fill={groundColor} stroke="#000000" strokeWidth="6" />
      </svg>
    </div>
  );
};

/** 11. Cementerio Arqueológico de Homínidos Extintos en la Niebla */
export const CementerioHominidosNieblaStage: React.FC<{ frame: number }> = ({ frame }) => {
  const fogShift = Math.sin(frame * 0.08) * 45;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#070D19] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="graveSky" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#091122" />
            <stop offset="100%" stopColor="#1E293B" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="1920" height="790" fill="url(#graveSky)" />
        {/* Luna pálida velada */}
        <circle cx="1630" cy="185" r="68" fill="#CBD5E1" opacity="0.28" />

        {/* Siluetas lejanas de monolitos de basalto en profundidad de campo */}
        {[180, 420, 1480, 1740].map((mx, i) => (
          <path
            key={`mono-${i}`}
            d={`M ${mx - 38} 790 L ${mx - 32} ${610 + (i % 2) * 35} Q ${mx} ${575 + (i % 2) * 35} ${mx + 32} ${610 + (i % 2) * 35} L ${mx + 38} 790 Z`}
            fill="#0F172A"
            stroke="#000000"
            strokeWidth="4"
            opacity="0.7"
          />
        ))}

        {/* Capas de niebla baja deslizándose suavemente */}
        <ellipse cx={640 + fogShift} cy="760" rx="620" ry="52" fill="#94A3B8" opacity="0.16" />
        <ellipse cx={1360 - fogShift} cy="785" rx="680" ry="58" fill="#CBD5E1" opacity="0.14" />

        {/* Suelo rocoso sombrío */}
        <rect x="0" y="790" width="1920" height="290" fill="#0F172A" stroke="#000000" strokeWidth="6" />
      </svg>
    </div>
  );
};

/** 12. Abismo del Cuello de Botella Genético (Oscuridad Africana y Círculo Cálido de Brasa) */
export const AbismoCuelloBotellaFuegoStage: React.FC<{ frame: number }> = ({ frame }) => {
  const emberRadius = 280 + Math.sin(frame * 0.18) * 18;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#03050A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <rect x="0" y="0" width="1920" height="1080" fill="#03050A" />

        {/* Silueta cartográfica tenue del continente africano en el fondo nocturno */}
        <path
          d="M 830 170 L 1010 170 L 1110 280 L 1185 385 L 1105 520 L 1045 715 L 955 755 L 895 585 L 775 415 L 755 270 Z"
          fill="#0F172A"
          stroke="#1E293B"
          strokeWidth="4"
          opacity="0.65"
        />

        {/* Único círculo cálido de supervivencia en el centro */}
        <circle cx="960" cy="760" r={emberRadius} fill="#EA580C" opacity="0.18" />
        <circle cx="960" cy="775" r={emberRadius * 0.52} fill="#FACC15" opacity="0.16" />

        {/* Suelo nocturno casi en penumbra total */}
        <rect x="0" y="795" width="1920" height="285" fill="#090D16" stroke="#000000" strokeWidth="6" />
      </svg>
    </div>
  );
};

/** 13. Epílogo: Disolución del Museo hacia el Amanecer Dorado de la Sabana con Gran Acacia */
export const AmanecerSabanaAcaciaStage: React.FC<{ frame: number }> = ({ frame }) => {
  // En los primeros 70 frames las paredes laterales de hormigón del museo se disuelven hacia el amanecer
  const museumFade = Math.max(0, 1 - frame / 75);
  const sunRiseY = Math.max(485, 565 - frame * 0.08);
  const breeze = Math.sin(frame * 0.12) * 5;

  return (
    <div className="absolute inset-0 pointer-events-none z-0 bg-[#FDE68A] overflow-hidden">
      <svg className="w-full h-full" viewBox="0 0 1920 1080">
        <defs>
          <linearGradient id="epilogueDawn" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#1E3A8A" />
            <stop offset="35%" stopColor="#F97316" />
            <stop offset="75%" stopColor="#FDBA74" />
            <stop offset="100%" stopColor="#FEF08A" />
          </linearGradient>
        </defs>

        {/* Cielo de amanecer africano monumental */}
        <rect x="0" y="0" width="1920" height="790" fill="url(#epilogueDawn)" />

        {/* Sol naciente dorado en el tercio derecho con haces volumétricos */}
        <circle cx="1490" cy={sunRiseY} r="145" fill="#FEF08A" opacity="0.38" />
        <circle cx="1490" cy={sunRiseY} r="96" fill="#FDE047" stroke="#000000" strokeWidth="5" />
        {[-24, -10, 6, 22].map((ang, i) => (
          <polygon
            key={`ray-${i}`}
            points={`1490,${sunRiseY} ${1050 + i * 210},0 ${1160 + i * 210},0`}
            fill="#FEF9C3"
            opacity="0.11"
          />
        ))}

        {/* Llanura lejana con siluetas pacíficas de cebras, antílopes y aves cruzando hacia el sol */}
        <path d="M 0 790 Q 520 735 1080 765 Q 1520 735 1920 790 Z" fill="#B45309" stroke="#000000" strokeWidth="4" />
        {[1180, 1270, 1365, 1610].map((ax, i) => (
          <g key={`herd-${i}`} transform={`translate(${ax + ((frame * 0.25) % 80)}, 752)`}>
            <ellipse cx="0" cy="0" rx="18" ry="9" fill="#291003" />
            <line x1="-11" y1="6" x2="-11" y2="22" stroke="#291003" strokeWidth="3" />
            <line x1="10" y1="6" x2="10" y2="22" stroke="#291003" strokeWidth="3" />
            <path d="M 14 -4 L 22 -20 L 29 -18" fill="none" stroke="#291003" strokeWidth="4" strokeLinecap="round" />
          </g>
        ))}
        {/* Bandada de aves africanas en el cielo dorado */}
        {[0, 1, 2, 3, 4].map((b) => (
          <path
            key={`bird-${b}`}
            d={`M ${1180 + b * 56} ${290 - b * 16 + breeze} Q ${1192 + b * 56} ${278 - b * 16 + breeze} ${1204 + b * 56} ${290 - b * 16 + breeze}`}
            fill="none"
            stroke="#1E293B"
            strokeWidth="3.5"
          />
        ))}

        {/* GRAN ÁRBOL DE ACACIA AFRICANA en el tercio izquierdo (sombra donde se sientan el Stickman y el chimpancé) */}
        <g transform="translate(360, 790)">
          {/* Tronco robusto inclinado y ramas extendidas */}
          <path
            d="M -45 0 C -35 -140, -55 -280, -20 -430 C 10 -320, 28 -160, 42 0 Z"
            fill="#451A03"
            stroke="#000000"
            strokeWidth="7"
          />
          <path d="M -22 -385 L -230 -495 M -15 -415 L 15 -535 M 5 -375 L 265 -485" stroke="#451A03" strokeWidth="18" strokeLinecap="round" />
          {/* Copas aparasoladas de acacia mecidas por la brisa */}
          <ellipse cx={-210 + breeze} cy="-510" rx="195" ry="44" fill="#15803D" stroke="#000000" strokeWidth="6" />
          <ellipse cx={245 + breeze} cy="-500" rx="215" ry="46" fill="#16A34A" stroke="#000000" strokeWidth="6" />
          <ellipse cx={10 + breeze} cy="-555" rx="270" ry="54" fill="#22C55E" stroke="#000000" strokeWidth="6" />
        </g>

        {/* Colina de pasto dorado en primer término */}
        <rect x="0" y="790" width="1920" height="290" fill="#D97706" stroke="#000000" strokeWidth="6" />
        <path d="M 0 790 Q 460 760 940 795 L 940 1080 L 0 1080 Z" fill="#65A30D" stroke="#000000" strokeWidth="5" />

        {/* Disolución inicial de las paredes de hormigón del museo de la Escena 1 */}
        {museumFade > 0.01 && (
          <g opacity={museumFade}>
            <rect x="0" y="0" width="320" height="1080" fill="#1E293B" stroke="#000000" strokeWidth="6" />
            <rect x="1600" y="0" width="320" height="1080" fill="#1E293B" stroke="#000000" strokeWidth="6" />
          </g>
        )}
      </svg>
    </div>
  );
};
