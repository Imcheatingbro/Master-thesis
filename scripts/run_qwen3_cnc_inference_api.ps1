param(
    [ValidateSet("best", "bf16_best", "hard_v2_e3_final", "base")]
    [string]$Variant = "best",

    [ValidateRange(1, 65535)]
    [int]$Port = 8000,

    [string]$ApiKey = "llamafactory-local",

    [string]$LlamaFactoryCli = "llamafactory-cli"
)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$resolvedCli = Get-Command $LlamaFactoryCli -ErrorAction SilentlyContinue

$variantConfig = @{
    best = @{
        Config = "configs\finetuning\qwen3_8b_cnc_qlora_best_api.yaml"
        Model = "qwen3-8b-cnc-qlora-best"
    }
    bf16_best = @{
        Config = "configs\finetuning\qwen3_8b_cnc_bf16_lora_best_api.yaml"
        Model = "qwen3-8b-cnc-bf16-lora-best"
    }
    hard_v2_e3_final = @{
        Config = "configs\finetuning\qwen3_8b_cnc_bf16_lora_hard_v2_e3_final_api.yaml"
        Model = "qwen3-8b-cnc-bf16-lora-hard-v2-e3-final"
    }
    base = @{
        Config = "configs\finetuning\qwen3_8b_cnc_base_api.yaml"
        Model = "qwen3-8b-base"
    }
}

if (-not $resolvedCli) {
    throw "LLaMA-Factory CLI not found: $LlamaFactoryCli"
}
$LlamaFactoryCli = $resolvedCli.Source

$selected = $variantConfig[$Variant]
$configPath = Join-Path $projectRoot $selected.Config
if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) {
    throw "Inference config not found: $configPath"
}

$env:API_HOST = "127.0.0.1"
$env:API_PORT = [string]$Port
$env:API_KEY = $ApiKey
$env:API_MODEL_NAME = $selected.Model

Write-Host "Variant: $Variant"
Write-Host "Model ID: $($selected.Model)"
Write-Host "Endpoint: http://127.0.0.1:$Port/v1"
Write-Host "Config: $configPath"
Write-Host "Stop the server with Ctrl+C."

Push-Location $projectRoot
try {
    & $LlamaFactoryCli api $configPath
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
