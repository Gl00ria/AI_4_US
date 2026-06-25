#
# roughly estimate the GB required to run a model
#
# - BF16 = 16-Bit = 2 Bytes
# - Q8 = 8-Bit = 1 Byte
# - Q6 = 6-Bit = 0.75 Byte
# - Q5 = 5-Bit = 0.62 Byte
# - Q4 = 4-Bit = 0.5 Byte
# - Q3 = 3-Bit = 0.37 Byte
# - Q2 = 2-Bit = 0.25 Byte
# - Q1 = 1-Bit = 0.12 Byte
#

def model_memory_estimate(
    total_params,
    bits_per_parameter,
    context_tokens=8192,
    active_params_b=3,   # MoE active params
    vram_gb=8,
    ram_gb=32
):

    #
    # MODEL WEIGHTS
    #
    weights_gb = total_params * bits_per_parameter / 8 / 1e9

    #
    # KV CACHE (MoE APPROX)
    #
    kv_cache_gb = (
        active_params_b
        * (context_tokens / 8192)
        * 0.08
    )

    total_gb = weights_gb + kv_cache_gb

    #
    # FIT CHECK
    #
    if total_gb <= vram_gb:
        status = "Fits in VRAM"
    elif total_gb <= ram_gb:
        status = "Does fit your system, but doesn't fit in VRAM (CPU offload required)"
    else:
        status = "Does NOT fit your system (even with CPU offload)"

    #
    # SAFE CONTEXT ESTIMATE
    #
    safe_context = int(
        max(
            0,
            (vram_gb - weights_gb) / (active_params_b * 0.08) * 8192
        )
    )

    safe_context = max(512, safe_context)

    #
    # OUTPUT
    #
    print("\n========= Input =========")
    print(f"Total Params: {total_params:,}")
    print(f"Active Params (MoE): {active_params_b:,}")
    print(f"Quantization: {bits_per_parameter}-bit")
    print(f"Context: {context_tokens:,} tokens")

    print("\n=== Estimated MEMORY ===")
    print(f"Weights: {weights_gb:.2f} GB")
    print(f"KV Cache: {kv_cache_gb:.2f} GB")
    print(f"TOTAL: {total_gb:.2f} GB")

    print(f"\n=== System Check CHECK ({vram_gb} GB GPU, {ram_gb} GB RAM) ===")
    print(f"Status: {status}")


#
# EXAMPLE (your model)
#
model_memory_estimate(
    total_params=35_000_000_000,
    bits_per_parameter=4,
    context_tokens=262144,
    active_params_b=3,
    vram_gb=8,
    ram_gb=32
)

