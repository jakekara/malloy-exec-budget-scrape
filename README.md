# Scrape of agency budgents in governor's executive order

This PDF has lots of tables:

So, I wanted CSVs.

I asked for them.

I didn't get them.

I ran the Section B pages of the PDF through Comet Docs to get one giant
[CSV file](data/Just Section B - Sheet2.csv)

I wrote [scrape_it.py](scrape_it.py) to walk through the CSV file and pull
out the parts that are actually tables, store them in the [output](output)
dir and ignore the rest.

The file [mega](output/mega.csv) combines all of the sheets into one CSV.

I can't vouch for the complete accuracy of these scrapes.
