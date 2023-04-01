import cv2



def main():
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # flip image
        cv2.imshow("YOLOv8", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    cv2.waitKey(1)
    cv2.destroyAllWindows()

    print("Hello")




if __name__=="__main__":
    main()