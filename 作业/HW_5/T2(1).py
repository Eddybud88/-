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
        extracted_file_path = os.path.splitext(file_path)[0]
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

    def gtf_to_bed(self, gtf_path, bed_path):
        try:
            with open(gtf_path, 'r', encoding='utf-8') as gtf_file, open(bed_path, 'w', encoding='utf-8') as bed_file:
                printed_lines = 0
                for line in gtf_file:
                    if line.startswith('#'):
                        continue

                    parts = line.strip().split('\t')
                    if len(parts) >= 6:
                        bed_line = '\t'.join(parts[:6]) + '\n'
                        bed_file.write(bed_line)

                        if printed_lines < 3:
                            print(bed_line.strip())
                            printed_lines += 1
            print(f"GTF to BED conversion completed. BED file saved at {bed_path}")
        except Exception as e:
            print(f"An error occurred during the conversion: {e}")

    def remove_file(self, filename):
        try:
            os.remove(filename)
            print(f"File {filename} has been removed.")
        except Exception as e:
            print(f"Failed to remove file {filename}: {e}")


    def main(self, url):
        gtf_path, compressed_path = self.download_and_extract(url)
        bed_path = os.path.join(self.target_dir, os.path.splitext(os.path.basename(gtf_path))[0] + '.bed')

        self.gtf_to_bed(gtf_path, bed_path)

        self.remove_file(gtf_path)
        self.remove_file(compressed_path)
        self.remove_file(bed_path)

if __name__ == "__main__":
    url = "http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz"
    target_dir = 'C:\\Users\\admin\\Desktop'
    processor = GTFFileProcessor(target_dir)
    processor.main(url)
