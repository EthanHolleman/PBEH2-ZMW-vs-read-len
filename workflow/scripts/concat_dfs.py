import pandas as pd


paths = snakemake.input['frames']
frames = [pd.read_csv(path, sep='\t') for path in paths]
concat = pd.concat(frames).reset_index()
concat.to_csv(snakemake.output['out'], sep='\t', index=False)
