
import os


class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        #aws s3 sync /path/to/local/directory s3://your-bucket-name
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        #aws s3 sync s3://your-bucket-name /path/to/local/directory
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)

