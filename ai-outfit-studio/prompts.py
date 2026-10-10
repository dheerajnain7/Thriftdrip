"""100 unique AI outfit prompts for ThriftDrip's MY TYPE OUTFIT series.

Each prompt follows the proven formula tested on 2026-10-10:
headless faceless model + trending piece + color + white studio + photorealistic.
"""

TOPS = [
    ("oversized hoodie", ["black", "beige", "white", "grey", "olive"]),
    ("zip-up hoodie", ["beige", "black", "grey", "navy"]),
    ("oversized sweatshirt", ["white", "black", "beige", "brown"]),
    ("cargo jacket", ["olive", "black", "beige"]),
    ("denim jacket", ["blue", "black", "light-wash"]),
    ("flannel shirt", ["red-check", "green-check", "black-check"]),
    ("striped long-sleeve tee", ["black-and-white", "navy-and-white"]),
    ("fitted baby tee", ["black", "white", "grey"]),
    ("knit cardigan", ["beige", "brown", "grey"]),
    ("bomber jacket", ["black", "olive", "navy"]),
]

BOTTOMS = [
    ("extremely baggy washed denim jeans", ["dark-blue", "black", "light-blue", "grey"]),
    ("baggy cargo pants", ["black", "olive", "beige", "grey"]),
    ("wide-leg jeans", ["blue", "black", "white"]),
    ("baggy sweatpants", ["black", "grey", "beige"]),
]

SHOES = ["chunky white sneakers", "black sneakers", "white sneakers"]

BASE_STYLE = (
    "headless faceless fashion model, no face, no head visible, "
    "full-body shot, pure white studio background, soft studio lighting, "
    "subtle shadow under shoes, photorealistic, premium streetwear editorial, "
    "Pinterest fashion inspiration, 9:16 vertical"
)


def build_prompts(count=100):
    """Return `count` unique outfit prompts (deterministic order)."""
    prompts = []
    i = 0
    for top, top_colors in TOPS:
        for bottom, bottom_colors in BOTTOMS:
            for tc in top_colors:
                for bc in bottom_colors:
                    shoe = SHOES[i % len(SHOES)]
                    prompts.append(
                        f"{BASE_STYLE}, wearing {tc} {top} layered naturally, "
                        f"{bc} {bottom}, {shoe}, "
                        f"model standing naturally with hands in pockets"
                    )
                    i += 1
                    if len(prompts) >= count:
                        return prompts
    return prompts


PROMPTS_100 = build_prompts(100)


if __name__ == "__main__":
    print(f"Total prompts: {len(PROMPTS_100)}")
    print("Unique:", len(set(PROMPTS_100)) == len(PROMPTS_100))
    for n, p in enumerate(PROMPTS_100[:3], 1):
        print(f"\n[{n}] {p[:120]}...")
