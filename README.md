# brendan_eos_reweighting_example

Quick example for Brendan's EOS reweighting applications

## Installing and running jester

- Installing `jester`: [docs page](https://nuclear-multimessenger-astronomy.github.io/jester/index.html#installation)
- Running `jester`, general info: [this docs page](https://nuclear-multimessenger-astronomy.github.io/jester/inference/workflow.html)
- More info on the EOS reweighting in [this example](https://nuclear-multimessenger-astronomy.github.io/jester/examples/inference/reweighting/reweighting.html)

## What is in this repo

- `nicer`: This shows how to use EOS reweighting with the NICER likelihoods. This is just a random collection of the available datasets Check out [this docs page](https://nuclear-multimessenger-astronomy.github.io/jester/overview/likelihoods/nicer.html) to see which datasets are available and perhaps switch out a few of them.
- `simulation`: This shows how to take an EOS curve (here, an npz file, but just any format works), generate a bunch of mock mass-radius observations into a JSON file in the correct format for `jester` and then run `jester`.
- `test_prior`: Ignore. This is just for me to get an EOS set to be used in reweighting, but you have your own.
