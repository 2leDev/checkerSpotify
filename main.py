import subprocess

# Function to execute PowerShell script for each token
def redeem_spotify_code(token):
    powershell_script = fr'''
    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.124 Safari/537.36"
    $session.Cookies.Add((New-Object System.Net.Cookie("sss", "1", "/", "www.spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_t", "f783b73ccee1b5a631cf44abcf7029cc", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_m", "us", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_landing", "https%3A%2F%2Fwww.spotify.com%2Fus%2Fpremium%2F%3Futm_source%3Dus-en_brand_contextual_text%26utm_medium%3Dpaidsearch%26utm_campaign%3Dalwayson_ucanz_us_performancemarketing_core_brand%2Bcontextual%2Btext%2Bus-en%2Bgoogle", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_landingref", "https%3A%2F%2Fwww.google.com%2F", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_adid", "b6efea6f-a8cd-467a-8b3a-e928060f8766", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gcl_au", "1.1.1069102453.1719337454", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_tt_enable_cookie", "1", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ttp", "Q-4cPo34rS1z0Ih0cviWwzCe70M", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_scid", "850b13bd-5837-425b-9031-7f877fad2f34", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gid", "GA1.2.486718524.1719337454", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_cs_c", "0", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_fbp", "fb.1.1719337455993.684777628397070651", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_sctr", "1%7C1719298800000", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("justRegistered", "1", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_dc", "AQDGZ4DPMmJc5yaiemuc2d2VDZoKL_YfG7BvEcod0mJC3-Ips930JzTjgMp-kDQZqjqPukOwo6cpfwlEB_uoU_2_DYhvBr3MhaiE4rnQcXKglXnla9o8iFFVVxuj_OXDuUzmQNX0iG8Cg4muTGR_IkSUBn6j1hYN", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_gaid", "0088fcdf549322cd24c4709e8ee68df3445d806b1545e99ad15f55", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("payment-sdk-locales", "en%2Cen%2Cen", "/", "www.spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_scid_r", "850b13bd-5837-425b-9031-7f877fad2f34", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_S0T2DJJFZM", "GS1.1.1719337580.1.0.1719337581.0.0.0", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_cs_id", "fe5e40ae-928b-a5b6-b036-d8370311a3fa.1719337454.2.1719340789.1719340789.1.1753501454611.1", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gcl_gs", "2.1.k1`$i1719355640", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_cs_mk_ga", "0.9606023118040783_1719355640831", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gac_UA-5784146-31", "1.1719355649.*", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_ZWG1NSHWD8", "GS1.1.1719355672.1.0.1719355672.0.0.0", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("sp_last_utm", "%7B%22utm_campaign%22%3A%22your_account%22%2C%22utm_medium%22%3A%22menu%22%2C%22utm_source%22%3A%22spotify%22%7D", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga", "GA1.2.1055112787.1719337454", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_S35RN5WNT2", "GS1.1.1719355641.3.1.1719355680.0.0.0", "/", ".spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("__Host-sp_csrf_sid", "c3cb6adb8721ff4f8bab227e453a0d4594595f9025978357d31cd5dd357a1b4e", "/", "www.spotify.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("OptanonConsent", "isGpcEnabled=0&datestamp=Tue+Jun+25+2024+15%3A48%3A01+GMT-0700+(Mountain+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=BG169%3A1%2Ct00%3A1%2Ci00%3A1%2CBG170%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1%2Cf11%3A1&AwaitingReconsent=false", "/", ".spotify.com")))
    Invoke-WebRequest -UseBasicParsing -Uri "https://www.spotify.com/us/redeem/v2/api/redeem/" `
    -Method "POST" `
    -WebSession $session `
    -Headers @{{
        "authority"="www.spotify.com"
        "method"="POST"
        "path"="/us/redeem/v2/api/redeem/"
        "scheme"="https"
        "accept"="*/*"
        "accept-encoding"="gzip, deflate, br, zstd"
        "accept-language"="en-US,en;q=0.9"
        "origin"="https://www.spotify.com"
        "referer"="https://www.spotify.com/us/redeem/"
        "sec-fetch-dest"="empty"
        "sec-fetch-mode"="cors"
        "sec-fetch-site"="same-origin"
        "x-csrf-token"="013acda7198e7406e8c5fcbdbcd0a4d23bc6142ae031373139333535363739393039"
    }} `
    -ContentType "text/plain;charset=UTF-8" `
    -Body "{{\\"token\\":\\"{token}\\",\\"recaptchaValue\\":\\"03AFcWeA4s65y3x82onygwYFBz6kdFGNL31wn-9LHtYtlH8yrY1Zc1rhSmmmiUX2IJkKeahNlQxJeSZYJTJG0pMfZ9B0AMs8aWmsM0wHZyx77kN6qv7O6by-Urva9ablHF61INoIqLSAA0ecPAgSqqPVfhx1UdtZbObp_6LmQ6mJEugqT4c5yFrg2Kg23TCXkgSWJQhH_svf_GLissh4TLPjSigyklyW8rouEiDjcUSN9RkgNEGiGVJD5XjUbdBDyd10EMmF0vDcWBViCmm1wXfz0u1P5g8MTveCX54NxXWQxyacw_1D1m1MUdg4fQ0hzjZZCqnPpawvC_1veUHHacN-bYS9CrrXEZVWonCLKiSQOKfHHW4KFql3x_8ll0-CtMl6sXlHbbQ4yLHr2fNM_TCwu5owk8Psv3yttWNjwkMQwy6Ry1fwI5MdhcAk_Ohl1hXOpnNAcF-2-NzG3_4kckCedeq6zSXLInjZczp_aOlHkLthKjbkNQGy1sR_yHlk3vFyHiXwcbMLEURJ07FWdw_YnuOGrNA7nNWC9L2Ciye8dXX0-_LBtWoI28_LiPz7t44UfIq0JVQ8lHAnoM0IYfMm3TGQibRt0Gh1Lk33hI1bFESiBz8x4TXfPPrEAWJhhiAlso_y-1L6Xg-jRKhkE0BGurgMNDSh2jQc-QLlqItmQgHg0M18yGrhI\\"}}"
    '''

    try:
        result = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True)
        if 'StatusCode        : 400' in result.stdout:
            print(f"Invalid | {token}")
        else:
            print(f"Valid | {token}")
    except Exception as e:
        print(f"Error processing token {token}: {str(e)}")

# Main function to read file and process tokens
def main():
    filename = input("Enter the filename with tokens (e.g., spotifycode.txt): ")

    try:
        with open(filename, 'r') as file:
            tokens = file.readlines()
            for token in tokens:
                token = token.strip()  # Remove newline characters or spaces
                redeem_spotify_code(token)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {str(e)}")

if __name__ == "__main__":
    main()
