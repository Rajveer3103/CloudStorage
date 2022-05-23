import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="sl.BGM-jN6qcuFTTO8hNXdKN32Gvt3jUrWLVK5ZOdbNDsz1820anHL0b0-82DLkOUsSI6gTlcNnaK65qOF4QfwWpt2B41Sc8ijMXyzR1rmjfcOvsCgsO8fveyC7GcOL9vi4heD8gpGieTfP"
    transferData= TransferData(access_token)
    file_from=input("Enter the File Path to Transfer")
    file_to= input("Enter the Full Path to Upload to Dropbox")
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")

main()
