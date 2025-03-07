import pandas as pd

def read_olympics_data(url):

    #read and clean data
    df = pd.read_html(url)[2]
    df = df[13:-3]
    df["Year"] = df["Games"].str[:4]
    df["Year"] = df["Year"].astype(int)
    df["Total"] = df["Total"].astype(int)
    df = df[["Year", "Total"]]
    return df

if __name__ == "__main__":  
    #for testing purpose
    url = "https://en.wikipedia.org/wiki/Sweden_at_the_Olympics"
    df = read_olympics_data(url)
    print(df.info())
