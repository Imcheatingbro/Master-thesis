param(
    [ValidateSet("smoke", "train")]
    [string]$Mode = "smoke",

    [string]$LlamaFactoryCli = "llamafactory-cli",

    [string]$PythonExe = "python",

    [string]$HuggingFaceCache = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ResolvedCli = Get-Command $LlamaFactoryCli -ErrorAction SilentlyContinue
$ResolvedPython = Get-Command $PythonExe -ErrorAction SilentlyContinue

if (-not $ResolvedCli) {
    throw "LLaMA-Factory CLI not found: $LlamaFactoryCli"
}
if (-not $ResolvedPython) {
    throw "Python executable not found: $PythonExe"
}
$LlamaFactoryCli = $ResolvedCli.Source
$PythonExe = $ResolvedPython.Source

& $PythonExe -c "import unsloth, torch; assert torch.cuda.is_available(); print('Unsloth/CUDA check: PASS')"
if ($LASTEXITCODE -ne 0) {
    throw "The Unsloth or CUDA environment check failed."
}

if ($HuggingFaceCache) {
    $env:HF_HOME = $HuggingFaceCache
    $env:HF_HUB_CACHE = $HuggingFaceCache
}
$env:HF_XET_HIGH_PERFORMANCE = "1"
$env:PYTORCH_CUDA_ALLOC_CONF = "expandable_segments:True"
$env:CUDA_VISIBLE_DEVICES = "0"
$env:TOKENIZERS_PARALLELISM = "false"
$env:TENSORBOARD_LOGGING_DIR = Join-Path $ProjectRoot "outputs\finetuning\qwen3_8b_cnc_bf16_lora_unsloth_v1\tensorboard"

$ConfigName = if ($Mode -eq "smoke") {
    "qwen3_8b_cnc_bf16_lora_unsloth_smoke.yaml"
} else {
    "qwen3_8b_cnc_bf16_lora_unsloth_v1.yaml"
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
