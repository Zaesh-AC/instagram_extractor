def get_image_path(post):
    return post[0].split("/")

def get_image_source(post):
    return get_image_path(post)[:3]

def get_image_filename(post):
    return get_image_path(post)[3:4][0]

def get_file_path(post):
    source = "/".join(get_image_source(post))
    filename = get_image_filename(post)
    return f"data/{source}/{filename.split('.')[0]}"

def get_context_data():
    return {
        "title": "Instagram Data Extractor",
        "home_text": "Home text",
        "description": "Desc",
        "instructions": "Inst",
        "": "",
    }