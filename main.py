from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        # type='photo',
        # color='blackandwhite',
        # size='large',
        license='noncommercial',
        # date=((2022, 7, 2), (2022, 7, 3)) 
    )
    crawler = GoogleImageCrawler(storage={'root_dir': '.\img'})
    crawler.crawl(
        keyword='Prague',
        max_num=5,
        # min_size=(1000,1000),
        overwrite=True,
        # filters=filters,
        file_idx_offset='auto'
    )

def main():
    google_img_downloader()
    
    
if __name__ == '__main__':
    main()
