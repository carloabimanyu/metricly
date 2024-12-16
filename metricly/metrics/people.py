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


def cost_per_hire(total_recruiting_cost, total_hires):
    """
    Calculate the Cost Per Hire, the average cost to recruit a single employee.

    Args:
        total_recruiting_cost (array-like): Total recruiting costs.
        total_hires (array-like): Total number of hires.

    Returns:
        float: The cost per hire.
    """
    recruiting_sum, hires_sum = validate_and_sum(total_recruiting_cost, total_hires)
    if hires_sum == 0:
        raise ValueError("Total hires must be greater than zero.")
    return recruiting_sum / hires_sum


def turnover_rate(total_separation, total_employee):
    """
    Calculate the Turnover Rate, the proportion of employees who left the company.

    Args:
        total_separation (array-like): Total number of separations.
        total_employee (array-like): Total number of employees.

    Returns:
        float: The turnover rate.
    """
    separation_sum, employee_sum = validate_and_sum(total_separation, total_employee)
    if employee_sum == 0:
        raise ValueError("Total employees must be greater than zero.")
    return separation_sum / employee_sum


def course_completion_rate(total_completed_employee, total_enrolled_employee):
    """
    Calculate the Course Completion Rate, the proportion of employees who completed a course.

    Args:
        total_completed_employee (array-like): Total employees who completed the course.
        total_enrolled_employee (array-like): Total employees enrolled in the course.

    Returns:
        float: The course completion rate.
    """
    completed_sum, enrolled_sum = validate_and_sum(total_completed_employee, total_enrolled_employee)
    if enrolled_sum == 0:
        raise ValueError("Total enrolled employees must be greater than zero.")
    return completed_sum / enrolled_sum


def assessment_pass_rate(total_passed_employee, total_enrolled_employee):
    """
    Calculate the Assessment Pass Rate, the proportion of employees who passed an assessment.

    Args:
        total_passed_employee (array-like): Total employees who passed the assessment.
        total_enrolled_employee (array-like): Total employees enrolled in the assessment.

    Returns:
        float: The assessment pass rate.
    """
    passed_sum, enrolled_sum = validate_and_sum(total_passed_employee, total_enrolled_employee)
    if enrolled_sum == 0:
        raise ValueError("Total enrolled employees must be greater than zero.")
    return passed_sum / enrolled_sum


def training_spend_rate(total_training_spend, total_operating_cost):
    """
    Calculate the Training Spend Rate, the proportion of operating costs spent on training.

    Args:
        total_training_spend (array-like): Total training spend.
        total_operating_cost (array-like): Total operating costs.

    Returns:
        float: The training spend rate.
    """
    training_sum, operating_sum = validate_and_sum(total_training_spend, total_operating_cost)
    if operating_sum == 0:
        raise ValueError("Total operating costs must be greater than zero.")
    return training_sum / operating_sum


def training_cost_per_employee(total_training_cost, total_enrolled_employee):
    """
    Calculate the Training Cost Per Employee, the average cost of training per employee.

    Args:
        total_training_cost (array-like): Total training costs.
        total_enrolled_employee (array-like): Total employees enrolled in training.

    Returns:
        float: The training cost per employee.
    """
    training_cost_sum, enrolled_sum = validate_and_sum(total_training_cost, total_enrolled_employee)
    if enrolled_sum == 0:
        raise ValueError("Total enrolled employees must be greater than zero.")
    return training_cost_sum / enrolled_sum


def average_performance_rating(total_performance_rating, total_employee):
    """
    Calculate the Average Performance Rating per employee.

    Args:
        total_performance_rating (array-like): Total performance ratings given.
        total_employee (array-like): Total employees evaluated.

    Returns:
        float: The average performance rating.
    """
    rating_sum, employee_sum = validate_and_sum(total_performance_rating, total_employee)
    if employee_sum == 0:
        raise ValueError("Total employees must be greater than zero.")
    return rating_sum / employee_sum


def performance_review_completion_rate(total_completed_reviews, total_scheduled_reviews):
    """
    Calculate the Performance Review Completion Rate.

    Args:
        total_completed_reviews (array-like): Total completed performance reviews.
        total_scheduled_reviews (array-like): Total scheduled performance reviews.

    Returns:
        float: The performance review completion rate.
    """
    completed_sum, scheduled_sum = validate_and_sum(total_completed_reviews, total_scheduled_reviews)
    if scheduled_sum == 0:
        raise ValueError("Total scheduled reviews must be greater than zero.")
    return completed_sum / scheduled_sum


def absence_rate(total_absence_days, total_working_days):
    """
    Calculate the Absence Rate, the proportion of working days employees were absent.

    Args:
        total_absence_days (array-like): Total days of employee absence.
        total_working_days (array-like): Total working days.

    Returns:
        float: The absence rate.
    """
    absence_sum, working_sum = validate_and_sum(total_absence_days, total_working_days)
    if working_sum == 0:
        raise ValueError("Total working days must be greater than zero.")
    return absence_sum / working_sum


def promotion_rate(total_promotion, total_employee):
    """
    Calculate the Promotion Rate, the proportion of employees promoted.

    Args:
        total_promotion (array-like): Total promotions given.
        total_employee (array-like): Total employees.

    Returns:
        float: The promotion rate.
    """
    promotion_sum, employee_sum = validate_and_sum(total_promotion, total_employee)
    if employee_sum == 0:
        raise ValueError("Total employees must be greater than zero.")
    return promotion_sum / employee_sum


def hr_to_employee_ratio(total_hr, total_employee):
    """
    Calculate the HR to Employee Ratio.

    Args:
        total_hr (array-like): Total HR staff.
        total_employee (array-like): Total employees.

    Returns:
        float: The HR to employee ratio.
    """
    hr_sum, employee_sum = validate_and_sum(total_hr, total_employee)
    if employee_sum == 0:
        raise ValueError("Total employees must be greater than zero.")
    return hr_sum / employee_sum


def salary_hike(current_salary, previous_year_salary):
    """
    Calculate the Salary Hike percentage.

    Args:
        current_salary (array-like): Current year salaries.
        previous_year_salary (array-like): Previous year salaries.

    Returns:
        float: The salary hike percentage.
    """
    current_sum, previous_sum = validate_and_sum(current_salary, previous_year_salary)
    if previous_sum == 0:
        raise ValueError("Previous year salaries must be greater than zero.")
    return (current_sum - previous_sum) / previous_sum
