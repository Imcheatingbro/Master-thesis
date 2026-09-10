param(
    [ValidateSet("smoke", "train")]
    [string]$Mode = "smoke",

    [string]$LlamaFactoryCli = "llamafactory-cli",

    [string]$HuggingFaceCache = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ResolvedCli = Get-Command $LlamaFactoryCli -ErrorAction SilentlyContinue

if (-not $ResolvedCli) {
    throw "LLaMA-Factory CLI not found: $LlamaFactoryCli"
}
$LlamaFactoryCli = $ResolvedCli.Source

if ($HuggingFaceCache) {
    $env:HF_HOME = $HuggingFaceCache
    $env:HF_HUB_CACHE = $HuggingFaceCache
}
$env:HF_XET_HIGH_PERFORMANCE = "1"
$env:PYTORCH_CUDA_ALLOC_CONF = "expandable_segments:True"
$env:CUDA_VISIBLE_DEVICES = "0"
$env:TOKENIZERS_PARALLELISM = "false"
$env:TENSORBOARD_LOGGING_DIR = Join-Path $ProjectRoot "outputs\finetuning\qwen3_8b_cnc_qlora_v1\tensorboard"

$ConfigName = if ($Mode -eq "smoke") {
    "qwen3_8b_cnc_qlora_smoke.yaml"
} else {
    "qwen3_8b_cnc_qlora_v1.yaml"
}
$ConfigPath = Join-Path $ProjectRoot "configs\finetuning\$ConfigName"

Push-Location $ProjectRoot
try {
    & $LlamaFactoryCli train $ConfigPath
    if ($LASTEXITCODE -ne 0) {
        throw "LLaMA-Factory training failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
