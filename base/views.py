from django.shortcuts import render
from django.views.generic import base as BaseView

class BaseView():
    method_only = ['GET']
    def main(self):
        # セッションから遷移元リストを取得し、最後尾のパスをリダイレクト先に設定する
        back_redirect_histories = self.request.session['back_redirect_histories']
        self.redirect_to = back_redirect_histories[-1]
    # def view(cls, request, **kwargs):
       
    #     try:
    #         this.main()
    #     except ApplicationException as ae:
    #         # 業務例外発生時
    #         ...
    #         ..
    #         .
    #     else:
    #         cls.__update_back_redirect_histories(request) # request.META.HTTP_REFERERをセッションにつめる処理
    #     return this.response()

    def __update_back_redirect_histories(request):
        """ このメソッド追加
        """
        # 戻るボタン押下時は何もしない
        if 'back' in request.path:
            return

        # リファラ(遷移元)をセッションに保存する処理
        back_redirect_histories = list()
        if 'HTTP_REFERER' in request.META and request.META['HTTP_REFERER']:
            # 既に遷移元のリストがセッションに存在する場合はそのリストに追加する。
            if 'back_redirect_histories' in request.session:
                back_redirect_histories = request.session['back_redirect_histories']
            if len(back_redirect_histories) == 0 or back_redirect_histories[-1] != request.build_absolute_uri():
                back_redirect_histories.append(request.META['HTTP_REFERER'])

            # 遷移元リストを後方から走査し、現在のURLと一致するリファラが見つかった場合、
            # リファラの最後尾から見つかった位置までのリファラをリストから削除する。
            rm_index = 0
            for redirect in reversed(back_redirect_histories):
                rm_index += 1
                if redirect == request.build_absolute_uri():
                    rm_index = -rm_index # 正数を負数に変換
                    break;
            if rm_index < 0:
                back_redirect_histories = back_redirect_histories[:rm_index]

            # 新しい遷移元リストでセッションを更新
            request.session['back_redirect_histories'] = back_redirect_histories
