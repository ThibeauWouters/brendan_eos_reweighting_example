from pathlib import Path
import numpy as np
from jesterTOV.inference.result import InferenceResult

INPUT_PATH = Path(__file__).parent / "outdir" / "results.h5"
OUTPUT_PATH = Path(__file__).parent / "outdir" / "prior_jester.npz"


def main() -> None:
    print(f"Loading {INPUT_PATH} ...")
    result = InferenceResult.load(INPUT_PATH)

    masses = np.asarray(result.posterior["masses_EOS"])
    lambdas = np.asarray(result.posterior["Lambdas_EOS"])
    radii = np.asarray(result.posterior["radii_EOS"])
    ids = np.arange(masses.shape[0], dtype=np.int64)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.savez(OUTPUT_PATH, masses=masses, lambdas=lambdas, radii=radii, ids=ids)

    print(f"Saved to {OUTPUT_PATH}")
    print(f"  masses : {masses.shape}")
    print(f"  lambdas: {lambdas.shape}")
    print(f"  radii  : {radii.shape}")
    print(f"  ids    : {ids.shape}")


if __name__ == "__main__":
    main()
