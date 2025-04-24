import pandas as pd
import news_injection
import stock_data_injection


portfolio_df= stock_data_injection.portfolio
portfolio_price_df= stock_data_injection.portfolio_price
news_data_df= news_injection.news_data
news_data_df.info()



#converting datetime to date in news dataset

news_data_df['datetime'] = pd.to_datetime(news_data_df['datetime'], errors= 'coerce')#.dt.date
news_data_df.rename(columns={'datetime':'date'}, inplace =True)



def dataframe_overview(df):
    #display basic information about dataframe 
    print('Dataframe Info:\n')
    df.info()

    #display the description of datframe 
    print('\n Dataframe Description:\n')
    print(df.describe())
    
    #display for the null value presrnt in the dataframe
    print("\n Check null value in Dataframe: \n")
    print(df.isnull().sum())

    #display for the duplicate values in the dataframe
    print('\n Check Duplicate values in Datafrme: \n')
    print(df.duplicated().sum())
    
    # display the unique values present in the Dataframe
    print('\n Check the unique values of dataframe: \n')
    print(df.nunique())

    #display the column details of each dataframe
    print('\n Column Description: \n')
    print(list(df.columns))

    # display the shape of each dataframe
    print('\n Shape of Dataframe (Rows,Colums):\n')
    print(df.shape)

    #display the data type of dataframe
    print('\n Data type of Each Column in Dataframe: \n ')
    print(df.dtypes)

    return 


# passing datafame to dataframe_overview 

print('\n Displaying the Overview of Portfolio dataframe: \n')
dataframe_overview(portfolio_df)

print('\n Displaying the Overview of Portfolio Prices  dataframe: \n')
dataframe_overview(portfolio_price_df)

print('\n Displaying the Overview of News dataframe: \n')
dataframe_overview(news_data_df)


def trim (df):

    #Strip the leading anf trailing whitespaces form column name 
    df.columns = df.columns .str.strip()

    # droping the duplicates rows
    df= df.drop_duplicates()

    #Convert all column name into lowercase 
    df.columns= df.columns.str.lower()

    # Convert all column names to lowercase for consistency
    df.columns = df.columns.str.lower()

    # Replace spaces in column names with underscores for easier access
    df.columns = df.columns.str.replace(' ', '_')

    # Select columns with object data types (categorical/textual data)
    df_obj = df.select_dtypes(['object'])

    # Convert object type columns to string and strip whitespace from each value
    df[df_obj.columns] = df_obj.apply(lambda x: x.astype(str).str.strip())

    # Print confirmation message after cleaning
    print("All column names cleaned, duplicates dropped, and text columns processed.")

    print("clean dataset \n")
    print(df.head())
    return df

# Applying the cleaning Function on all datafrmes avalible 

#Applying the trim fuction to portfolio dataframe.
print("\n Clean Portfolio Dataset")
portfolio_data_clean= trim(portfolio_df)

#Applying the trim fuction to portfolio price dataframe.
print("\n Clean Portfolio Price Dataset")
portfolio_price_data_clean= trim(portfolio_price_df)

#Applying the trim fuction to news dataframe.
print("\n Clean News Dataset")
news_data_clean= trim(news_data_df)


#drop close from portfoli_data_clean
portfolio_data_clean.drop('close',axis=1, inplace= True)
portfolio_data_clean.head()

portfolio_merge= pd.merge(portfolio_price_data_clean,portfolio_data_clean,
                        on = ['ticker'],how= "inner")

print('\n Merge Dataset: \n')
print(portfolio_merge)