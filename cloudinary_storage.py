import cloudinary
import cloudinary.uploader
import json
import sys

sys.path.append("/home/rifatsoftdev/MyLinux")
from Secure import secure


PATH = "/home/rifatsoftdev/MyLinux/Json/cloudinary_storage.json"


class CloudinaryStorage:
    def __init__(self, cloud_name, api_key, api_secret):
        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret
        )

    def upload_file(self, file_path, public_id=None, file_type="image"):
        """
        file_type: image | video | raw
        """
        result = cloudinary.uploader.upload(
            file_path,
            resource_type=file_type,
            # public_id=public_id,
            overwrite=True
        )

        return {
            "public_id": result["public_id"],
            "url": result["secure_url"]
        }

    def delete_file(self, public_id, file_type="image"):
        """
        public_id: id obtained during upload
        """
        result = cloudinary.uploader.destroy(
            public_id,
            resource_type=file_type
        )

        return result



if __name__ == "__main__":
    cloudinaryStorage = CloudinaryStorage(
        secure.CLOUD_NAME,
        secure.API_KEY,
        secure.API_SECRET
    )

    try:
        with open(PATH, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    while (True):
        print("1. Upload File")
        print("2. Delete File")
        print("3. Exit")

        try:
            num = int(input("Enter Number : "))
        except ValueError:
            print("Invalid Input.")
            continue

        if num == 1:
            file_path = input("Enter File Path : ")

            response = cloudinaryStorage.upload_file(
                file_path=file_path,
                # public_id="auroraslpabfgsrdlnw",
                file_type="image"
            )
            print(response)

            # save json file
            data.append(response)
            # save data
            with open(PATH, 'w') as file:
                json.dump(data, file, indent=4)
            print("File info saved to JSON.")

        elif (num == 2):
            public_id_to_delete = input("Enter Public ID to delete: ")
            cloudinaryStorage.delete_file(public_id_to_delete)

            found = False
            for i, item in enumerate(data):
                if item['public_id'] == public_id_to_delete:
                    found = True
                    del data[i]  # remove from list
                    break

            if found:
                with open(PATH, 'w') as file:
                    json.dump(data, file, indent=4)
                print(f"{public_id_to_delete} removed from JSON.")
            else:
                print("Public ID not found in JSON.")

        elif (num == 3):
            break

        else:
            print("Invalid Input.")


