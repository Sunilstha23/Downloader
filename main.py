from youtube_download import down_youtube

from image import dl_jpg

from mp3_downloader import obtain_data_from_bensound, save_to_disk

def downloader():
    perform ="""
    choose to form the task:
    1. youtube videos downloader
    2. image downloader
    3. mp3 dowloader
    4. exit
    """

    while True:
        print(perform)
        to_do = input('enter a number to perform task')

        if to_do == '1':
            link = input('enter youtube url here')
            down_youtube(link)


        elif to_do =='2':
            url = input('Enter img URl to download:')

            file_name = input('Enter file name to save as:')

            dl_jpg(url,'./images/', file_name)

        elif to_do =='3':
            mp3 = input('enter url of mp3 download')
            content = obtain_data_from_bensound(mp3)
            file_name = input('enter the song name')

            save_to_disk(data=content,filename=file_name, extension=".mp3")


        elif to_do =='4':
            break
        else:
            print ('invalid number')


if __name__ == "__main__":
    downloader()

