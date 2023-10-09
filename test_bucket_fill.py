from bucket_fill import fill, load_image, show_image


def normal_test_pattern(file):
    """
    Test: Normal Case
    Input: Seed Point is valid: within the image, not a boundary pixel
    Expected Outcome: A region of the image is filled
    """
    
    image = load_image(file)
    
    print("Test: Normal Case")
    print("Expected Outcome: A region of the image is filled")
    seed_point_normal = (10, 2)
    print(f"Seed Point: {seed_point_normal}")
    
    print("Before Filling:")
    show_image(image)
    
    image_normal = fill(image=image, seed_point=seed_point_normal)
    print("Filled Image:")
    show_image(image_normal)
    

def boundary_test_pattern(file):
    """
    Test: Boundary Case
    Input: Seed Point is a boundary pixel
    Expected Outcome: The image is unchanged
    """
    
    image = load_image(file)
    
    print("Test: Boundary Case")
    print("Expected Outcome: The image is unchanged")
    seed_point_boundary = (2, 3)
    print(f"Seed Point: {seed_point_boundary}")

    print("Before Filling:")
    show_image(image)
    
    image_boundary = fill(image=image, seed_point=seed_point_boundary)
    print("Filled Image:")
    show_image(image_boundary)
    

def out_of_bounds_test_pattern(file):
    """
    Test: Out of Bounds Case
    Input: Seed Point is out of bounds
    Expected Outcome: The image is unchanged
    """
    
    image = load_image(file)
    
    print("Test: Out of Bounds Case")
    print("Expected Outcome: The image is unchanged")
    seed_point_out_of_bounds = (100, 100)
    print(f"Seed Point: {seed_point_out_of_bounds}")
    
    print("Before Filling:")
    show_image(image)
    
    image_out_of_bounds = fill(image=image, seed_point=seed_point_out_of_bounds)
    print("Filled Image:")
    show_image(image_out_of_bounds)


def invalid_seed_points_test_pattern(file):
    """
    Test: Invalid Seed Points Case (i.e. negative values)
    Input: Seed Point has negative values
    Expected Outcome: The image is unchanged
    """
    
    image = load_image(file)
    
    print("Test: Invalid Seed Points Case")
    print("Expected Outcome: The image is unchanged")
    seed_point_invalid = (-10, 100)
    print(f"Seed Point: {seed_point_invalid}")
    
    print("Before Filling:")
    show_image(image)
    
    image_invalid = fill(image=image, seed_point=seed_point_invalid)
    print("Filled Image:")
    show_image(image_invalid)


if __name__ == '__main__':
    file = "data/snake.txt"
    normal_test_pattern(file)
    print("*"*100)
    boundary_test_pattern(file)
    print("*"*100)
    out_of_bounds_test_pattern(file)   
    print("*"*100)
    invalid_seed_points_test_pattern(file)
    