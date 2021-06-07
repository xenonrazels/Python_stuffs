import speedtest
test=speedtest.Speedtest()
test.get_servers()
best=test.get_best_server()
print(f"Found: {best['host']} in {best['country']}")
print("Testing Download Speed...")

download_result=test.download()
print("Testing Upload Speed...")
upload_result=test.upload()
ping_result=test.results.ping

print(f"Download Speed: {download_result/8 /1024 / 1024:.2f} MB/s")
print(f"Upload Speed : {upload_result/8/1024/1024:.2f} MB/s")
print(f"Ping: {ping_result:.2f} ms")