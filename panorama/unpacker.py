from sqlalchemy.util import b

packed_code_f = open("code.pbin", "rb")
packed_code = packed_code_f.read()
log = ""

root_entry = packed_code.find(b"<root>")

while root_entry != -1:
    root_end = packed_code.find(b"</root>", root_entry)
    slash_start = packed_code[:root_entry].rfind(b"\\")
    filename = str(packed_code[slash_start+1:root_entry])[2:-1]
    endfile = filename.find(".xml")
    filename = filename[:endfile+4]
    code = packed_code[root_entry:root_end+7]

    print(f"[*] Found XML file {filename}")
    log += f"[*] Found XML file {filename}\n"

    unpacked_file = open("layout/" + filename, "wb")
    unpacked_file.write(code)
    unpacked_file.close()

    root_entry = packed_code.find(b"<root>", root_end)

js_entry = packed_code.find(b"panorama\\scripts\\")

while js_entry != -1:
    js_end = packed_code.find(b"PK", js_entry)  # idk what is it, but is eof sig
    filename_end = packed_code.find(b".js", js_entry) + 3

    filename = str(packed_code[js_entry+17:filename_end])[2:-1]
    code = packed_code[packed_code.find(b";", filename_end)+1:js_end]

    print(f"[*] Found JS file {filename}")
    log += f"[*] Found JS file {filename}\n"
    unpacked_file = open("scripts/" + filename, "wb")
    unpacked_file.write(code)
    unpacked_file.close()

    js_entry = packed_code.find(b"panorama\\scripts\\", js_end)


css_entry = packed_code.find(b"panorama\\styles\\")

while css_entry != -1:
    css_end = packed_code.find(b"PK", css_entry)
    filename_end = packed_code.find(b".css", css_entry) + 4

    filename = str(packed_code[css_entry + 16:filename_end])[2:-1]
    code = packed_code[filename_end+1:css_end]

    print(f"[*] Found CSS file {filename}")
    log += f"[*] Found CSS file {filename}\n"
    unpacked_file = open("styles/" + filename, "wb")
    unpacked_file.write(code)
    unpacked_file.close()

    css_entry = packed_code.find(b"panorama\\styles\\", css_end)

packed_code_f.close()
log_f = open("log.log", "w", encoding="utf-8")
log_f.write(log)
log_f.close()