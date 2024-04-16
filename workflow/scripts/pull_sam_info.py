# Read pacbio sam file and pull out just the info I want from each read for
# plotting. Currently just getting the read length and ZMW hole number
# Send output to tsv file for plotting using R.

import pandas as pd 

SAMPLE = snakemake.params['sample']

def parse_sam_line(line):
    line_split = line.split('\t')

    return {
        'read_length': len(line_split[9]),
        'zmw': line_split[28].split(':')[-1],
        'sample': SAMPLE
    }


def parse_sam_file(filepath):

    data = []

    with open(filepath) as handle:
        
        for each_line in handle:
            each_line = each_line.strip()
            data.append(parse_sam_line(each_line))
    
    return pd.DataFrame(data)



def main():

    filepath = snakemake.input['path']
    sam_df = parse_sam_file(filepath)
    sam_df.to_csv(
        snakemake.output['out'], sep='\t', index=False
    )


if __name__ == '__main__':
    main()
