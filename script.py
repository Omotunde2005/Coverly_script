from gemini import analyse
from firecrawl_scraper import scrape


job_listing_url = "https://www.ycombinator.com/companies/firecrawl/jobs/EK9HRDs-founding-developer-relations-community-support"



# Scrape job description and analyse with Google gemini.
def scrape_and_analyse(**kwargs):
    
    # Scrape job description
    response = scrape(job_listing_url)

    if response["is_valid"]:
        result = analyse(
            job_description=response["job_details"],
            industry=kwargs.get("industry"),
            years=kwargs.get("years"),
            skills=kwargs.get("skills"),
            education=kwargs.get("education"),
            career=kwargs.get("career"),
            tools=kwargs.get("tools")
        )
        return result.text
    return False



# A sample test user data to use.
test_user_data = {
    "industry": "Technology",
    "years": "5 years",
    "skills": "Developer Relations, Community Building, Technical Writing, Public Speaking, API Integration, Content Creation",
    "educational_background": "Bachelor's in Computer Science from XYZ University",
    "career": (
        "Launched a developer community with 10,000+ members; "
        "Designed and hosted 50+ webinars and workshops on API best practices; "
        "Collaborated with 5 startups to improve API adoption rates by 40%; "
        "Published 20+ technical articles on developer tools, some featured on Hacker News."
    ),
    "tools_frameworks_technologies": "Postman, Swagger, GraphQL, FastAPI, Flask, JavaScript, Python, GitHub Actions, Discord, Slack, Discourse",
}


# Run script
try:
    # Analysis result
    result = scrape_and_analyse(**test_user_data)
    if not result:
        error_message = "The URL you submitted is either invalid, or contains no details about a job listing"
    else:
        print(result)
except Exception as e:
    print(e)
