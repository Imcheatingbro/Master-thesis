param(
    [ValidateSet("smoke", "train")]
    [string]$Mode = "smoke"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$LlamaFactoryCli = "D:\Anaconda3\envs\Model_finetune\Scripts\llamafactory-cli.exe"

if (-not (Test-Path -LiteralPath $LlamaFactoryCli)) {
    throw "找不到 Model_finetune 环境中的 llamafactory-cli：$LlamaFactoryCli"
}

$env:HF_HOME = "D:\huggingface_cache"
$env:HF_HUB_CACHE = "D:\huggingface_cache"
$env:HF_XET_HIGH_PERFORMANCE = "1"
$env:PYTORCH_CUDA_ALLOC_CONF = "expandable_segments:True"
$env:CUDA_VISIBLE_DEVICES = "0"
$env:TOKENIZERS_PARALLELISM = "false"

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
        throw "LLaMA-Factory 训练失败，退出码：$LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
