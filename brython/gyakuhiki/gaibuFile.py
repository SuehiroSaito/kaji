from browser import document, html
from browser.widgets.dialog import Dialog, InfoDialog

def show_dialog(ev):
    d = Dialog("ユーザー入力・設定")
    d.panel <= html.P("お名前を入力してください：")
    inp = html.INPUT(type="text", value="")
    d.panel <= inp
    d.panel <= html.BR()
    
    btn = html.BUTTON("送信")
    d.panel <= btn
    
    def on_submit(e):
        name = inp.value
        d.close()
        InfoDialog("結果", f"こんにちは、{name}さん！")
        
    btn.bind("click", on_submit)

document["button_01"].bind("click", show_dialog)