import pandas

squirrel_df=pandas.read_csv("Squirrel_Data.csv")

gray_squirrels_count=len(squirrel_df[squirrel_df["Primary Fur Color"]=="Gray"])
cinnammon_squirrels_count=len(squirrel_df[squirrel_df["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(squirrel_df[squirrel_df["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrels_count,cinnammon_squirrels_count,black_squirrels_count]
}

my_df=pandas.DataFrame(data_dict)
my_df.to_csv("Squirrel_Count.csv")
