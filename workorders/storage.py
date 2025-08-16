# workorders/storage.py
import os
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader

class CustomCloudinaryStorage(MediaCloudinaryStorage):
    """Custom storage that uploads documents as raw files"""
    
    def _upload(self, name, content):
        """Override upload to handle different file types"""
        # Get file extension
        ext = os.path.splitext(name)[1].lower()
        
        # Images - use default upload
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']:
            print(f"📸 Uploading image: {name}")
            return super()._upload(name, content)
        
        # Documents - upload as raw
        else:
            print(f"📄 Uploading document as raw: {name}")
            content.seek(0)  # Reset position
            return cloudinary.uploader.upload(
                content, 
                resource_type="raw",
                **self.upload_options
            )