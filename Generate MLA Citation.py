# Function to generate MLA citation
def generate_MLA_citation(author, title, publisher, year):
    citation = author + ". " + title + ". " + publisher + ", " + year + "."
    return citation

# Example usage
#Enter Author, Title, Publisher, Year
print(generate_MLA_citation("John Doe", "The History of Python", "ABC Publishing", "2020"))
