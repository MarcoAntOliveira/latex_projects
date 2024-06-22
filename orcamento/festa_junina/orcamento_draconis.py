import pandas as pd

# Step 1: Create DataFrame from the dictionary
orcamento =  {
    "URL": [
        "https://shopee.com.br/product/288720899/23492981314?d_id=de29b&uls_trackid=4vqqhlti00s6&utm_content=XrQoHsUQGSDgE7RsV4bsCbodNM5",
        "https://shopee.com.br/product/344441852/21112157396?d_id=de29b&uls_trackid=4vqqi7k500s6&utm_content=XrQoHsUQGMtU7MZszD8guRezs27",
        "https://shopee.com.br/Kit-Chaveiros-Variados-50-Unidade-Diferentes-Atacado-Lembrancinha-Festinha-Festa-i.344441852.19199231318?publish_id=&sp_atk=b8e96dd3-3b2e-4106-9448-b3cc9638229c&xptdk=b8e96dd3-3b2e-4106-9448-b3cc9638229c",
        "https://shopee.com.br/Kit-10-Chap%C3%A9us-de-Palha-Fof%C3%A3o-guri-Festa-Junina-Decora%C3%A7%C3%A3o-S%C3%A3o-Jo%C3%A3o-i.514351259.23197483000?sp_atk=ce84203b-b002-4e6e-8413-a413837b1c28&xptdk=ce84203b-b002-4e6e-8413-a413837b1c28"
    ],
    "Price": [42.79, 37.15, 49.50, 69.90]
}

df = pd.DataFrame(orcamento)

# Step 2: Save DataFrame to an Excel file
file_path = "orcamento.xlsx"
df.to_excel(file_path, index=False)

# Step 3: Read the Excel file back into a DataFrame
orcamento1 = pd.read_excel(file_path)

# Display the DataFrame to verify the content
print(orcamento1)
