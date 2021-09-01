import dropbox
class TransferData:
    def __init__(self,access_token) :
        self.access_token = access_token
    def upload_file(self,file_from,file_to):  
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
        access_token="ZOEl8pcyEvIAAAAAAAAAARrOPZaUyE8wRaMeHNqkgXhsGcgm0_FwEl7fWVqtk1oj"
        transferData=TransferData(access_token)
        file_from=input("enter File Path")
        file_to=input("enter path for dropbox")
        transferData.upload_file(file_from,file_to)
        print("files moved")
main()       


