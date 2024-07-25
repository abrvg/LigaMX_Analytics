import src.scrapper as scrapper
import src.team_info as ti

if __name__ == "__main__":
    
    query_type = "table"
    index = 0

    
    clubs = ti.club_info
    
    for club in clubs:
        scrapper.random_delay()
        url = clubs.get(club)
        
        if url != None:
            # S3 direction, create the right partitions for raw data
            file_name = 'raw/' + club + '.csv'
            
            df = scrapper.ImportHTML(url, query_type, index)
            df.to_csv(file_name)
            print(f"{file_name} saved")
    
    

