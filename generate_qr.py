import qrcode
import qrcode.image.svg as qr_svg

def create_simple_qr(data,name):
    img = qrcode.make(data)
    img.save(f"{name}.png")

    return img
def create_advance_qr(data,name_qr,border,size,fill_color,back_color):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CPRRECT_L,border=border,box_size=size)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color= back_color)
    img.save(f"{name_qr}.png")
    return img

def create_svg_qr(data,name):
    factory = qr_svg.SvgPathImage
    svg_image = qrcode.make(data,image_factory=factory)
    svg_image.save(f"{name}.png")

def create_qr_wifi(id,password,name): # working
    qr_wfi = qrcode.QRCode()
    qr_wfi.add_data(f"{id} {password}")
    qr_wfi.make_image().save(f"{name}.png")
    return qr_wfi

