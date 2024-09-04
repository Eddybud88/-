def parse_gene_data(gene_string):
    parts = gene_string.split('|')

    gene = []

    try:
        gene_name = parts[0].split(':')[1]
    except Exception as e:
        print(f"Error extracting gene name: {e}")
        gene_name = None

    for part in parts[1:]:
        if part:
            try:
                transcript, coding_change = part.split(':')
                coding_change = coding_change.split('(')[1].split(')')[0].split(';')[-1]
                gene.append([transcript, coding_change])
            except Exception as e:
                print(f"Error processing part '{part}': {e}")

    return gene_name, gene


if __name__ == "__main__":
    gene_string = "ENSG00000119714:GPR68|ENST00000238699:SYNONYMOUS_CODING(409;144;48;A;gcC/gcT)|ENST00000529102:SYNONYMOUS_CODING(455;114;38;A;gcC/gcT)|ENST00000531499:SYNONYMOUS_CODING(454;114;38;A;gcC/gcT)|ENST00000535815:SYNONYMOUS_CODING(455;114;38;A;gcC/gcT)|"

    gene_name, gene_details = parse_gene_data(gene_string)

    print(f"{gene_name}基因={gene_details}")
