import cv2

def open_ip_camera(ip_address):
    try:
        url = f"http://{ip_address}/video"
        cap = cv2.VideoCapture(url)

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Failed to grab frame")
                break

            cv2.imshow('IP Camera', frame)

            # Press 'q' key to exit the camera window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = "YOUR_IP_ADDRESS_HERE"
    open_ip_camera(ip_address)
