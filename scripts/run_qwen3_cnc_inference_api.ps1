param(
    [ValidateSet("bf16_best", "hard_v2_e3_final", "qwen14_final")]
    [string]$Variant = "bf16_best",

    [ValidateRange(1, 65535)]
    [int]$Port = 8000,

    [string]$ApiKey = "llamafactory-local",

    [string]$LlamaFactoryCli = "llamafactory-cli"
)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$resolvedCli = Get-Command $LlamaFactoryCli -ErrorAction SilentlyContinue

$variantConfig = @{
    bf16_best = @{
        Config = "configs\finetuning\qwen3_8b_cnc_bf16_lora_best_api.yaml"
        Model = "qwen3-8b-cnc-bf16-lora-best"
    }
    hard_v2_e3_final = @{
        Config = "configs\finetuning\qwen3_8b_cnc_bf16_lora_hard_v2_e3_final_api.yaml"
        Model = "qwen3-8b-cnc-bf16-lora-hard-v2-e3-final"
    }
    qwen14_final = @{
        Config = "configs\finetuning\qwen3_14b_cnc_qlora_final_api.yaml"
        Model = "qwen3-14b-cnc-qlora-final"
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
