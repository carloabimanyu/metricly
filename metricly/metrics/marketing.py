import numpy as np


def validate_and_sum(*arrays):
    """
    Validate inputs, ensure they are array-like, non-negative, and return their sums.
    
    Args:
        arrays (array-like): Input arrays to validate and sum.
    
    Returns:
        list: A list of summed values for the provided arrays.

    Raises:
        ValueError: If any input contains negative values or if sums are invalid.
        TypeError: If inputs are not array-like or cannot be converted to numeric.
    """
    summed_values = []
    for array in arrays:
        try:
            array = np.asarray(array, dtype=np.float64)
        except (ValueError, TypeError):
            raise TypeError("All inputs must be array-like and numeric.")
        
        if np.any(array < 0):
            raise ValueError("Inputs must not contain negative values.")
        
        summed_values.append(np.sum(array))
    
    return summed_values


def cost_per_mile(total_marketing_cost, total_impression):
    """
    Calculate the Cost Per Mille (CPM), the cost per 1,000 impressions.

    Args:
        total_marketing_cost (array-like): The total marketing costs.
        total_impression (array-like): The total impressions.

    Returns:
        float: The cost per 1,000 impressions (CPM).
    """
    marketing_sum, impression_sum = validate_and_sum(total_marketing_cost, total_impression)
    if impression_sum == 0:
        raise ValueError("Total impressions must be greater than zero.")
    return (marketing_sum / impression_sum) * 1000


def frequency(total_impression, total_reach):
    """
    Calculate the frequency metric, which is the average number of impressions per reach.

    Args:
        total_impression (array-like): The total number of impressions.
        total_reach (array-like): The total reach (unique viewers).

    Returns:
        float: The frequency, calculated as total_impression / total_reach.
    """
    impression_sum, reach_sum = validate_and_sum(total_impression, total_reach)
    if reach_sum == 0:
        raise ValueError("Total reach must be greater than zero.")
    return impression_sum / reach_sum


def ad_recall_lift(total_ad_recall, total_reach):
    """
    Calculate Ad Recall Lift, which measures the proportion of reach that recalls the ad.

    Args:
        total_ad_recall (array-like): Total ad recall numbers.
        total_reach (array-like): Total reach (unique viewers).

    Returns:
        float: The ad recall lift.
    """
    recall_sum, reach_sum = validate_and_sum(total_ad_recall, total_reach)
    if reach_sum == 0:
        raise ValueError("Total reach must be greater than zero.")
    return recall_sum / reach_sum


def engagement_rate(total_engagement, total_reach):
    """
    Calculate Engagement Rate, the proportion of reach that engages with the content.

    Args:
        total_engagement (array-like): Total engagement numbers.
        total_reach (array-like): Total reach (unique viewers).

    Returns:
        float: The engagement rate.
    """
    engagement_sum, reach_sum = validate_and_sum(total_engagement, total_reach)
    if reach_sum == 0:
        raise ValueError("Total reach must be greater than zero.")
    return engagement_sum / reach_sum


def post_engagement_rate(total_engagement, total_followers):
    """
    Calculate Post Engagement Rate, the proportion of followers engaging with a post.

    Args:
        total_engagement (array-like): Total engagement numbers.
        total_followers (array-like): Total follower count.

    Returns:
        float: The post engagement rate.
    """
    engagement_sum, follower_sum = validate_and_sum(total_engagement, total_followers)
    if follower_sum == 0:
        raise ValueError("Total followers must be greater than zero.")
    return engagement_sum / follower_sum


def click_through_rate(total_click, total_impression):
    """
    Calculate Click-Through Rate (CTR), the proportion of impressions that result in clicks.

    Args:
        total_click (array-like): Total number of clicks.
        total_impression (array-like): Total impressions.

    Returns:
        float: The click-through rate.
    """
    click_sum, impression_sum = validate_and_sum(total_click, total_impression)
    if impression_sum == 0:
        raise ValueError("Total impressions must be greater than zero.")
    return click_sum / impression_sum


def cost_per_click(total_marketing_cost, total_click):
    """
    Calculate Cost Per Click (CPC), the cost for each click.

    Args:
        total_marketing_cost (array-like): The total marketing costs.
        total_click (array-like): Total number of clicks.

    Returns:
        float: The cost per click.
    """
    marketing_sum, click_sum = validate_and_sum(total_marketing_cost, total_click)
    if click_sum == 0:
        raise ValueError("Total clicks must be greater than zero.")
    return marketing_sum / click_sum


def cost_per_lead(total_marketing_cost, total_leads):
    """
    Calculate Cost Per Lead (CPL), the cost for each lead generated.

    Args:
        total_marketing_cost (array-like): The total marketing costs.
        total_leads (array-like): Total number of leads.

    Returns:
        float: The cost per lead.
    """
    marketing_sum, leads_sum = validate_and_sum(total_marketing_cost, total_leads)
    if leads_sum == 0:
        raise ValueError("Total leads must be greater than zero.")
    return marketing_sum / leads_sum
