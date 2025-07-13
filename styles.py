html_styles = """
    <style>
        .stMainBlockContainer {
            max-width:70rem;
        },
    </style>
    """

# Navigation bar styles
navbar_styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "40rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

# Navigation options
navbar_options = {
    "show_menu": True,
    "show_sidebar": False,
    "use_padding": False,
}

# Visualization specification for Pygwalker
vis_spec = r"""{"config":[{"config":{"defaultAggregated":false,"geoms":["auto"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"bedrooms","name":"bedrooms","basename":"bedrooms","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"bathrooms","name":"bathrooms","basename":"bathrooms","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"stories","name":"stories","basename":"stories","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"mainroad","name":"mainroad","basename":"mainroad","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"guestroom","name":"guestroom","basename":"guestroom","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"basement","name":"basement","basename":"basement","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"hotwaterheating","name":"hotwaterheating","basename":"hotwaterheating","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"airconditioning","name":"airconditioning","basename":"airconditioning","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"parking","name":"parking","basename":"parking","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"prefarea","name":"prefarea","basename":"prefarea","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"furnishingstatus","name":"furnishingstatus","basename":"furnishingstatus","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"price","name":"price","basename":"price","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"area","name":"area","basename":"area","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"price","name":"price","basename":"price","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"columns":[{"fid":"area","name":"area","basename":"area","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"color":[],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_Nl3O","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"raw","fields":["area","price"]}]}]}],"version":"0.4.9.15"}"""

# Style for the result text in Prediction
result_style = "color:green; font-weight:bold;"
def styled_result(result_text):
    return f'<div style="color:green; font-weight:bold; font-size: 30px; padding-bottom:13px; padding-top: 22px;">Predicted Price: {result_text}</div>'

# Developer information for the About page
fontawesome_css = '''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'''

reeve_info = {
    "name": "Reeve Wong",
    "Introduction": "With over 10 years of experience in application development and 2 years in GIS, I specialize in integrating spatial data systems and developing enterprise applications. My expertise spans across GIS technologies, Java-based systems, and AI applications, with a strong focus on solving complex technical challenges.",
    "linkedin": "https://www.linkedin.com/in/reeve-wong-279a78163/",
    "portfolio": "https://saitchihang.github.io/portfolio/"}

kevin_info = {
    "name": "Kevin Kovacik",
    "Introduction": "To be confirmed",
    "linkedin": "To be confirmed",
    "portfolio": "To be confirmed"}

developers = [reeve_info, kevin_info]

def developer_name_markdown(name_text):
    markdown_string = "<div style='display: flex; align-items: center; height: 40px;'>" + \
                        f"<h2 style='pointer-events: none; margin: 0;'>{name_text}</h2></div>"
    return markdown_string

def developer_portfolio_markdown(portfolio_url):
    markdown_string = "<div style='display: flex; align-items: center; height: 40px;'>"  + \
                        "<i class='fa-regular fa-address-card'></i>" + \
                        f"<a style='margin-left: 5px;' href='{portfolio_url}'> Portfolio </a></div>"
    return markdown_string

def developer_linkedin_markdown(linkedin_url):
    markdown_string = "<div style='display: flex; align-items: center; height: 40px;'>" + \
                        "<i class='fa-brands fa-linkedin'></i>" + \
                        f"<a style='margin-left: 5px;' href='{linkedin_url}'> linkedin </a></div>"
    return markdown_string

def developer_introduction_markdown(introduction_text):
    markdown_string = f"<div style='text-align: left; padding-top: 10px; padding-bottom: 10px;'>{introduction_text} </div>"
    return markdown_string