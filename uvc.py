#!/usr/bin/env python3

from winrt.windows.devices.enumeration import DeviceInformation
from winrt.windows.media.capture import MediaCapture, MediaCaptureInitializationSettings
from winrt.windows.media.devices import MediaDevice

import winrt.windows.media.capture as cap


def main():
    aqs_filter = MediaDevice.get_video_capture_selector()
    devices = DeviceInformation.find_all_async_aqs_filter(aqs_filter).get()
    device = devices[0]

    settings = MediaCaptureInitializationSettings()
    settings.video_device_id = device.id

    media_capture = MediaCapture()
    media_capture.initialize_with_settings_async(settings).get()

    # https://learn.microsoft.com/en-us/uwp/api/windows.media.devices.videodevicecontroller
    ctl = media_capture.video_device_controller

    # ok, exposure = ctl.exposure.try_get_value()
    # print(f"{ok=} {exposure=}")

    ok = ctl.try_set_powerline_frequency(cap.PowerlineFrequency.AUTO)
    print(f"{ok=}")

    ok, powerline_frequency = ctl.try_get_powerline_frequency()
    print(f"{ok=} {powerline_frequency=}")


if __name__ == "__main__":
    exit(main() or 0)
