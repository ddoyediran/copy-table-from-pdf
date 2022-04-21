import tabula

#df = tabula.read_pdf("https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf", pages="all")

pdf_path = "tables_sample.pdf"

df = tabula.read_pdf(pdf_path, pages="2")

#print(df)

# We can use these 2 methods if we are sure we only have one table on a page
df[0].to_csv("first_tb") # method 1: will create first_tb.csv 

# tabula.convert_into(pdf_path, "first_tb_2", output_format="csv", pages="1") # method 2: will create first_tb_2.csv 

# To extract multiple table from a single page
    # Note this will extract all the tables into a single worksheet
for i in range(len(df)):
    df[i].to_csv(f"page_2_tb{i}.csv") 


# To extract all tables from a single pdf
    # Note this will extract all the tables into a different worksheet

dfs = tabula.read_pdf(pdf_path, pages="all")

for i in range(len(dfs)):
    dfs[i].to_csv(f"all_pages_tb{i}.csv") 