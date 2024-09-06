import os
import requests
import gzip
import shutil


class GTFFileProcessor:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def download_and_extract(self, url):
        file_name = os.path.basename(url)
        file_path = os.path.join(self.target_dir, file_name)
        extracted_file_path = os.path.join(self.target_dir, os.path.splitext(file_name)[0])
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"{file_name} has been successfully downloaded")

            with gzip.open(file_path, 'rt', encoding='utf-8') as f_in, open(extracted_file_path, 'wt',
                                                                            encoding='utf-8') as f_out:
                shutil.copyfileobj(f_in, f_out)
            print(f"{os.path.splitext(file_name)[0]} has been successfully extracted")

            return extracted_file_path, file_path
        except requests.RequestException as e:
            print(f"Error downloading file from {url}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_file(self, filename):
        try:
            os.remove(filename)
            print(f"File {filename} has been removed.")
        except Exception as e:
            print(f"Failed to remove file {filename}: {e}")

    def count_genes_and_transcripts_on_chr19(self, gtf_path):
        gene_transcripts = {}
        gene_count = 0
        gene_id = None

        try:
            with open(gtf_path, 'r', encoding='utf-8') as gtf_file:
                for line in gtf_file:
                    if line.startswith('#'):
                        continue

                    parts = line.strip().split('\t')
                    if len(parts) < 9:
                        continue

                    chromosome, _, feature_type, _, _, _, _, _, attributes = parts
                    if chromosome == '19' and feature_type == 'gene':
                        gene_count += 1
                        gene_id = None
                        for attribute in attributes.split(';'):
                            key, value = attribute.strip().split(' ')
                            if key == 'gene_id':
                                gene_id = value.strip('"')
                                gene_transcripts[gene_id] = 0
                                break

                    elif chromosome == '19' and feature_type == 'transcript' and gene_id is not None:
                        gene_transcripts[gene_id] += 1

            print(f"Total number of genes on chr19: {gene_count}")
            return gene_transcripts
        except Exception as e:
            print(f"An error occurred while counting genes and transcripts: {e}")
            return None

    def main(self, url):
        gtf_path, compressed_path = self.download_and_extract(url)
        gene_transcripts = self.count_genes_and_transcripts_on_chr19(gtf_path)

        self.remove_file(gtf_path)
        self.remove_file(compressed_path)

        for gene_id, transcript_count in gene_transcripts.items():
            print(f"Gene ID: {gene_id}, Transcript Count: {transcript_count}")

if __name__ == "__main__":
    url = "http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz"
    target_dir = 'C:\\Users\\admin\\Desktop'
    processor = GTFFileProcessor(target_dir)
    processor.main(url)
