from collections import deque


def process_packets(packets, bufsize):
    # Stores the scheduled finish times for packets
    buffer = deque(maxlen=bufsize)

    start_times = [None] * len(packets)
    for i, (arrival, duration) in enumerate(packets):
        # Remove packets from the buffer that have been processed by the
        # arrival time.
        while buffer and buffer[0] <= arrival:
            buffer.popleft()

        if len(buffer) >= bufsize:
            # Buffer overrun
            start_times[i] = -1
        else:
            # This packet will start being processed after the finish time of
            # the last buffered packet (if there is anything in the buffer).
            start_times[i] = max(arrival, buffer[-1] if buffer else 0)

            # Store the scheduled finish time for this packet.
            buffer.append(start_times[i] + duration)
    return start_times


if __name__ == '__main__':
    s, n = list(map(int, input().split()))
    packets = []
    for i in range(n):
        packets.append(list(map(int, input().split())))
    times = process_packets(packets, s)
    for time in times:
        print(time)
