def replace_color(image, x, y, k):
    """
    Replace the color of the given pixel and all of its adjacent (excluding diagonally adjacent)
    same-colored pixels with the target color.

    Args:
        image (list[list[int]]): The matrix representing the image.
        x (int): The x-coordinate of the targeted pixel.
        y (int): The y-coordinate of the targeted pixel.
        k (int): The target color.

    Returns:
        list[list[int]]: The modified image.
    """
    rows, cols = len(image), len(image[0])
    target_color = image[x][y]
    
    if target_color == k:
        return image
    
    queue = [(x, y)]
    image[x][y] = k
    
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and image[ni][nj] == target_color:
                image[ni][nj] = k
                queue.append((ni, nj))
    
    return image