from whitenoise.middleware import WhiteNoiseMiddleware


class IndexWhiteNoise(WhiteNoiseMiddleware):
    """Adds support for serving index pages for directory paths."""

    INDEX_NAME = 'index.html'

    def update_files_dictionary(self, *args):
        super(IndexWhiteNoise, self).update_files_dictionary(*args)
        index_page_suffix = '/' + self.INDEX_NAME
        index_name_length = len(self.INDEX_NAME)
        directory_indexes = {}
        for url, static_file in self.files.items():
            if url.endswith(index_page_suffix):
                parent_directory_url = url[:-index_name_length]
                directory_indexes[parent_directory_url] = static_file
        self.files.update(directory_indexes)

    def find_file(self, url):
        print(url)
        if url.endswith('/'):
            url += self.INDEX_NAME
        return super(IndexWhiteNoise, self).find_file(url)