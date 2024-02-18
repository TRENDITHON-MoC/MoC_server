from PIL import Image
from io import BytesIO


class ImageCompressor:
    """
    이미지 압축 클래스
    """
    def post_size(image_file):
        """
        이미지 파일을 입력하면 압축된 이미지 파일을 리턴합니다.
        """
        image = Image.open(image_file)
        image = image.convert('RGB')

        image.thumbnail((2000, 2000))
        buffer = BytesIO()
        image.save(buffer, format = 'JPEG', quality = 80)
        buffer.seek(0)

        return buffer

    def thumbnail_size(image_file):
        image = Image.open(image_file)
        image = image.convert('RGB')

        image.thumbnail((500, 500))
        buffer = BytesIO()
        image.save(buffer, format = 'JPEG', quality = 80)
        buffer.seek(0)

        return buffer