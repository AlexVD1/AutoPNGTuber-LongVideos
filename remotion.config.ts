import { Config } from "@remotion/cli/config";
import { enableTailwind } from "@remotion/tailwind";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.setCrf(22);
Config.setConcurrency(4);
Config.overrideWebpackConfig((currentConfiguration) => {
  return enableTailwind(currentConfiguration);
});
