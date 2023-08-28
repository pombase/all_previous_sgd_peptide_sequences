set -e
mkdir -p data
# Download all the protein sequences from SGD releases
python get_sgd_data.py

# Make single line fasta (see script doc)
python make_single_line_fasta.py data/*.fasta

# iterate over sorted files, in pairs with a while loop, printing the diff between old
# and new release single line files, printing the lines that were removed only (old sequences)

prev=""
find data -name '*_single_line.tsv' | sort | while read -r next; do

    if [ "$prev" == "" ]; then
        prev=$next
        continue
    fi

    echo $prev $next
    # # file name without extension and without single_line
    next_name=$(basename $next _single_line.tsv)
    diff --unified=3 $prev $next| grep '^[-]'|tail -n +2 |cut -c2- | awk -v h="$next_name" '{print $0 "\t" h}'> data/${next_name}_diff.tsv

    prev=$next
done

# Concatenate all the diff files
cat data/*diff.tsv|sort|uniq > all_previous_seqs.tsv
