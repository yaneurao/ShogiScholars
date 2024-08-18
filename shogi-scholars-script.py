import os
import glob
import subprocess
import time

class USIEngine:
    def __init__(self, engine_path:str):
        self.engine = subprocess.Popen( engine_path,
                                        stdin   = subprocess.PIPE,
                                        stdout  = subprocess.PIPE,
                                        cwd     = os.path.dirname(engine_path),
                                        encoding= "UTF-8")

    def send_usi(self,command:str):
        ''' 思考エンジンにUSIコマンドを送信する。'''
        self.engine.stdin.write(command+"\n") # type:ignore
        self.engine.stdin.flush()             # type:ignore

    def wait_usi(self,wait_string:str):
        ''' 思考エンジンから指定した文字列が返ってくるまで待機する。'''
        while True:
            mes = self.receive_usi()
            if mes==wait_string: return
            time.sleep(0.1)

    def receive_usi(self)->str:
        ''' 思考エンジンから1行もらう。改行は取り除いて返す。'''
        line = self.engine.stdout.readline().strip() # type:ignore
        print(line) # for debug

        # エンジンのprocessが死んでたら例外を出す。
        if self.engine.poll() is not None:
            raise Exception("Engine is terminated.")
        return line

    def wait_for_quit(self):
        ''' エンジンの終了待ち。 '''
        while self.engine.poll() is None:
            time.sleep(0.1)

def main():
    # エンジン名と作者名
    print(f"id name shogi-scholars V1.00")
    print(f"id author yaneurao")

    # `engines`フォルダ配下にある `.exe`,`.bat`ファイルを探して、それらすべてを起動する。
    engine_paths = [file for ext in ["exe", "bat"] for file in glob.glob(f"engines/**/*.{ext}", recursive=True)]
    engines = [USIEngine(engine_path) for engine_path in engine_paths]

    while True:
        usi_input = input()
        commands = usi_input.split()
        if not commands:
            continue
        command = commands[0]

        # 以下のコマンドはそのままエンジンに転送してやる。
        if command in ('isready', 'setoption', 'usinewgame', 'gameover', 'position', 'go', 'stop', 'quit'):
            # `go`だけは、詰将棋エンジンに対しては`go mate`と変更する必要がある。
            for engine in engines:
                engine.send_usi(usi_input)

            # `isready`ならすべてのエンジンの`readyok`を待機して、すべてのエンジンから`readyok`が返ってきたら、`readyok`と出力する。
            if command == 'isready':
                for engine in engines:
                    engine.wait_usi('readyok')
                print("readyok")

            # `quit`なら全プロセスの終了待機をしてから終了
            elif command == "quit":
                for engine in engines:
                    engine.wait_for_quit()
                break

        else:
        # 対応していないUSIコマンドなので、エラー表示
            print(f"Unkwon Command : {command}")


if __name__ == "__main__":
    main()
