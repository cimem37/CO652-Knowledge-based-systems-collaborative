# ==========================================
# PC Tech Support Expert System by Bruno Cimo and Hishaam Mehmood 
# ==========================================
import sys

# -----------------------------
# THIS IS OUR KNOWLEDGE BASE (RULE-BASED SYSTEM)
# -----------------------------
bsod_errors = {
    "0x0000000A": {
        "error_name": "IRQL_NOT_LESS_OR_EQUAL",
        "consideration": "Different processes depending on dedicated or integrated GPU.",
        "solutions": [
            "Reinstall/update display and network drivers: uninstall through Device Manager on Windows. Right-click (uninstall option) on both network & display, as drivers will be installed automatically (as you removed all existing driver/settings of the machine) when you reboot the system. Windows Update may fix errors.",
            "Disk scan - Right-click local drive, properties, tools - check / Will do a check disk / error check on the next reboot, if required, before you get to the desktop. That fixes corrupt files on machine that cause blue screen.",
            "DISM /ONLINE /CLEANUP-IMAGE /RESTOREHEALTH - loads the most recent Windows restoration point - Windows creates one automatically.",
            "Then run SFC /SCANNOW - runs the Windows file system scan, reinstalls any corrupt system files."
        ]
    },
    "0x0000000D": {
        "error_name": "EXCEPTION_DOUBLE_FAULT",
        "consideration": "This BSOD is uncommon. BSOD error code 0x0000000D may also show 'MUTEX_LEVEL_NUMBER_VIOLATION' on the same blue screen.",
        "solutions": [
            "Restore a backup: Use installation or recovery media to get to startup settings.\n"
            "Insert the USB drive or DVD and restart your PC. If you’re using recovery media, skip the next step.\n"
            "On the Install Windows page, select 'Repair your computer'. (If you’re not seeing this page, your PC might not be set up to boot from a drive. Check your PC manufacturer’s info on how to change boot order and then try again.)\n"
            "On the Choose an option screen, select Troubleshoot > Advanced options > Startup Repair. Follow the onscreen instructions and check if you can boot the computer to desktop.",

            "If the issue persists, you may open PowerShell in administrator mode and run the following command.\n"
            "This reinstalls Windows default apps, which in turn can fix them:\n"
            "Get-AppxPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register “$($_.InstallLocation)\\AppXManifest.xml”}\n"
            "OR\n"
            "Get-AppXPackage | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register \"$($_.InstallLocation)\\AppXManifest.xml\"}",

            "DISM /ONLINE /CLEANUP-IMAGE /RESTOREHEALTH - Loads the most recent Windows restoration point (Windows creates one automatically, but this is NOT a backup).\n"
            "Then run SFC /SCANNOW - This runs the Windows file system scan and reinstalls any corrupt system files.\n"
            "Do a classic reboot.",

            "Reset Windows as a last resort."
        ]
    },
    "0x0000001E": {
        "error_name": "KMODE_EXCEPTION_NOT_HANDLED",
        "consideration": "This BSOD means that a kernel-mode program generated an exception which the error handler did not catch. BSOD error code 0x0000001E may also show 'KMODE_EXCEPTION_NOT_HANDLED' on the same blue screen.",
        "solutions": [
            "Back to normal system: The first thing to do when you meet 0x0000001E error is to restart your computer and make it back to the normal Windows system.\n"
            "How:\n"
            "- Hold your Power button for about 5 seconds to restart your computer.\n"
            "- If you can’t reboot your computer into normal mode in this way, you need to boot into Safe Mode. After that, restart the computer to see if the system has returned to normal.",

            "On your keyboard, press the Windows logo key and R together to invoke the Run box.\n"
            "Type 'devmgmt.msc' and click OK.\n"
            "In Device Manager, click on 'Display adapters' as well as 'Network adapters' and 'Storage controllers'.\n"
            "Right-click on your display device software and click Properties.\n"
            "Under the Driver tab, click 'Roll Back Driver', then follow the on-screen instructions to finish the process.",

            "If the Roll Back Driver option is grayed out, you can download a previous driver from the manufacturer’s website and install it on your PC.",

            "If the roll-back driver does not resolve this issue, you may have used the wrong driver or an outdated driver.\n"
            "There are two ways you can get the right drivers: manually or automatically.\n"
            "- Manual driver update: You can update your driver manually by going to the manufacturer’s website and searching for the most recent correct driver.\n"
            "- Be sure to choose only drivers that are compatible with your Windows version.",

            "If the issue persists, try uninstalling newly installed software:\n"
            "1) Click the Windows start button, type 'Control Panel' in the search box, and click Control Panel.\n"
            "2) Choose to view by 'Category' and then click 'Uninstall a program'.\n"
            "3) Find your newly installed program. Right-click on it and click 'Uninstall'.\n"
            "4) Follow the on-screen instructions and restart your computer to check if the blue screen error appears.\n"
            "5) Restart your computer and see if the issue is fixed.",

            "If the system is not fixed, perform a repair:\n"
            "1) On your keyboard, press the Windows logo key and R key at the same time to invoke the Run box.\n"
            "2) Type 'cmd' and press Shift+Ctrl+Enter together on your keyboard to open Command Prompt in administrator mode.\n"
            "3) Type 'sfc /scannow' and press Enter. Wait for the verification to be 100% complete.\n"
            "4) Restart your computer to check if the blue screen issue is fixed.\n"
            "If SFC can’t fix broken files, use the DISM tool by running: 'DISM /ONLINE /CLEANUP-IMAGE /RESTOREHEALTH' for deeper repair.",

            "Run a virus check and remove any detected malware using antivirus software (make sure it’s updated). If the antivirus scan does not fix the issue, try disabling/uninstalling your antivirus software and restarting your computer.",

            "Check your RAM:\n"
            "1) Plug your RAM in and out to make sure it is properly installed.\n"
            "2) Clean your RAM if it’s dusty, including the RAM slot.\n"
            "3) Reboot your computer to check if the problem persists.\n"
            "4) If not resolved, use the Windows Memory Diagnostics Tool:\n"
            "   - Press the Windows logo key + R to open the Run box.\n"
            "   - Type 'mdsched.exe' and click OK.\n"
            "   - Click 'Restart now and check for problems'.\n"
            "   - If the test result indicates a bad memory module, replace your RAM with a new one and restart your computer.",

            "Restore from a restore point:\n"
            "1) Press the Windows logo key + Pause together, then click 'System Protection'.\n"
            "2) Click 'System Restore'.\n"
            "3) Click 'Next' and choose a restore point where Windows didn’t show any errors.\n"
            "4) Follow the on-screen instructions to complete the process and restart your computer.\n"
            "If all else fails, reinstall Windows as a last resort. Be sure to back up your data before proceeding."
        ]
    },
    "0x00000050": {
        "error_name": "PAGE_FAULT_IN_NONPAGED_AREA",
        "consideration": "This BSOD means that invalid system memory has been referenced. BSOD error code 0x00000050 may also show 'PAGE_FAULT_IN_NONPAGED_AREA' on the same blue screen.\n"
                         "This indicates that invalid system memory has been referenced. This can be caused by a faulty driver. Antivirus software can also trigger this error, as can a corrupted NTFS volume.\n"
                         "It can also be caused by faulty hardware (in particular, faulty or overheated RAM or video RAM) or an overheated system component.",
        "solutions": [
            "Restart Your PC.",

            "Check System Temperature (Prevent Overheating Issues):\n"
            "- Use HWMonitor or Open Hardware Monitor to check CPU & GPU temperatures.\n"
            "- Ensure fans are working properly and clean any dust buildup.\n"
            "- If temperatures exceed 85°C, improve cooling or reapply thermal paste.",

            "Check and Remove Faulty Antivirus Software:\n"
            "- Temporarily disable or uninstall third-party antivirus software.\n"
            "- Restart your PC and check if the BSOD persists.\n"
            "- If the issue is resolved, switch to Windows Defender or a different antivirus.",

            "Reinstall or Update Drivers (Fix Faulty Drivers):\n"
            "- Open Device Manager (Win + X > Device Manager).\n"
            "- Look for devices with yellow exclamation marks.\n"
            "- Right-click the driver > Update Driver.\n"
            "- If updating doesn’t help, right-click and Uninstall the driver, then restart your PC.",

            "Run a Disk Check (Fix Disk Corruption):\n"
            "- Open Command Prompt as Administrator.\n"
            "- Type: chkdsk C: /f /r\n"
            "- Press Enter, then restart your PC to allow the scan to complete.",

            "Run Memory Diagnostic (Check for Faulty RAM or Video RAM):\n"
            "- Press Win + S, type Windows Memory Diagnostic, and open it.\n"
            "- Select 'Restart now and check for problems'.\n"
            "- Wait for the test to complete and check results in Event Viewer (eventvwr).\n"
            "- If RAM errors are found, replace the faulty memory module.",

            "Replace or Test with Different Hardware (Last Resort):\n"
            "- Test with a different RAM stick if you have multiple.\n"
            "- Try a different GPU if video memory is suspected.\n"
            "- Check for motherboard issues if RAM slots are faulty."
        ]
    },
    "0x0000003B": {
        "error_name": "SYSTEM_SERVICE_EXCEPTION",
        "solutions": [
            "Check Problematic Drivers:\n"
            "- Faulty drivers are the most common cause of this error.\n"
            "- Open PowerShell as Administrator.\n"
            "- Type 'verifier' and press Enter.\n"
            "- Select 'Create standard settings' > 'Automatically select unsigned drivers'.\n"
            "- Restart your PC and check for changes.",

            "Fix MBR and File System Errors:\n"
            "- Boot from Windows installation media.\n"
            "- Open Command Prompt from Advanced Options.\n"
            "- Run:\n"
            "  chkdsk c: /r\n"
            "  sfc /scannow\n"
            "- Restart your computer.",

            "Run Startup Repair:\n"
            "- Fixes many startup-related issues automatically.\n"
            "- Boot from installation media and select 'Repair your computer'.\n"
            "- Go to Troubleshoot > Advanced Options > Startup Repair.\n"
            "- Allow the process to complete.",

            "Perform a System Restore:\n"
            "- Roll back to a working state if the error began recently.\n"
            "- Go to Advanced Options > System Restore.\n"
            "- Select a restore point, confirm, and restart your PC.",

            "Disable Secure Boot:\n"
            "- Troubleshoot by disabling Secure Boot temporarily.\n"
            "- Enter BIOS (press F2, Esc, etc., during startup).\n"
            "- Navigate to the Security tab.\n"
            "- Disable Secure Boot, save settings, and restart.",

            "Reset BIOS:\n"
            "- Corrupt BIOS settings may cause system errors.\n"
            "- Enter BIOS settings.\n"
            "- Reset to defaults (e.g., Load Defaults or F9).\n"
            "- Save changes and restart.",

            "Run Display Context Record Command:\n"
            "- Debug system context to identify the cause.\n"
            "- Open Command Prompt as Administrator.\n"
            "- Run:\n"
            "  .cxr /w [Address]\n"
            "- (Replace [Address] with the correct context record.)",

            "Run Stack Backtrace Command:\n"
            "- Use for debugging system processes.\n"
            "- Use debugging tools to analyze stack frames (kd, kp commands).",

            "Rebuild BCD:\n"
            "- Fix critical boot loader issues.\n"
            "- Boot into Advanced Startup.\n"
            "- Open Command Prompt and run:\n"
            "  bootrec /fixmbr\n"
            "  bootrec /fixboot\n"
            "  bootrec /rebuildbcd\n"
            "- Restart your PC.",

            "Reinstall Windows (Last Resort):\n"
            "- Create a bootable USB/DVD with Windows.\n"
            "- Boot from it and follow installation instructions.\n"
            "- Complete the setup and restore your files."
        ]
    },
    "0x000000D1": {
        "error_name": "DRIVER_IRQL_NOT_LESS_OR_EQUAL",
        "consideration": "This BSOD means that a kernel-mode driver attempted to access pageable memory at a process IRQL that was too high. BSOD error code 0x000000D1 may also show 'DRIVER_IRQL_NOT_LESS_OR_EQUAL' on the same blue screen.",
        "solutions": [
            "Update or Roll Back Drivers:\n"
            "- Update: Ensure all drivers, especially for network adapters, graphics cards, and chipset drivers, are up to date.\n"
            "- Open Device Manager → Right-click on the suspected device → Update driver.\n"
            "- Roll Back: If the error started after a driver update, try reverting to the previous version:\n"
            "- Right-click the device → Properties → Driver tab → Roll Back Driver.",

            "Run Windows Update:\n"
            "- A Windows update can install critical patches or updated drivers that fix known issues.\n"
            "- Open Settings → Update & Security → Windows Update → Check for updates.",

            "Run System File Checker (SFC) and DISM:\n"
            "- Use these built-in tools to repair corrupted system files.\n"
            "- Open Command Prompt as an administrator.\n"
            "- Run the following commands:\n"
            "  sfc /scannow (Wait for the process to complete).\n"
            "  DISM /Online /Cleanup-Image /RestoreHealth.",

            "Test Hardware Components:\n"
            "- Check RAM using Windows Memory Diagnostic:\n"
            "- Search for 'Windows Memory Diagnostic' in the Start menu and follow the prompts.\n"
            "- If errors are detected, consider replacing the faulty RAM.",

            "Uninstall Problematic Software:\n"
            "- If you recently installed third-party antivirus software or system utilities, try uninstalling them.\n"
            "- Open Control Panel → Programs and Features → Right-click the software → Uninstall.",

            "Disable Overclocking:\n"
            "- Revert all overclocking settings to default in your BIOS or any overclocking software.",

            "Check for Malware:\n"
            "- Run a full system scan with Windows Security or a trusted antivirus program.",

            "Use Safe Mode:\n"
            "- Boot into Safe Mode to troubleshoot without third-party drivers.\n"
            "- Press Shift while restarting → Troubleshoot → Advanced Options → Startup Settings → Restart → Select Safe Mode.",

            "Perform a Clean Boot:\n"
            "- Temporarily disable non-Microsoft services and startup programs.\n"
            "- Press Win + R, type msconfig, and press Enter.\n"
            "- Go to the Services tab → Check 'Hide all Microsoft services' → Click 'Disable all'.\n"
            "- Disable all startup programs in Task Manager."
        ]
    },
    "0x1000007E": {
        "error_name": "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED",
        "solutions": [
            "Identify and Fix the Problematic Driver:\n"
            "- Press Windows + R, type 'eventvwr', and press Enter to open Event Viewer.\n"
            "- Expand Windows Logs > Select System > Look for errors with the identified problematic driver.\n"
            "- Once identified, update, disable, or uninstall the driver via Device Manager:\n"
            "  - Right-click the Start button > Select Device Manager.\n"
            "  - Right-click the problematic driver > Properties > Use 'Update Driver' or 'Roll Back Driver'.",

            "Boot into Safe Mode:\n"
            "- Restart your PC and repeatedly press the Del or F8 key during boot to access the Boot Menu.\n"
            "- Select Troubleshoot > Advanced Options > Startup Settings.\n"
            "- Enable Safe Mode by pressing the assigned key (e.g., F4).",

            "Roll Back Drivers:\n"
            "- Newly updated drivers may cause instability.\n"
            "- Open Device Manager.\n"
            "- Locate the problematic driver, right-click > Properties.\n"
            "- Navigate to the Driver tab and click 'Roll Back Driver' to return to the previous version.",

            "Run Memory Diagnostic Tool:\n"
            "- Open Windows Memory Diagnostic by searching for it in the Start menu.\n"
            "- Click 'Restart now and check for problems'.\n"
            "- Allow the diagnostic to complete and check results.",

            "Check Driver and Disk Health:\n"
            "- Corrupt drivers or disk errors can trigger this error.\n"
            "- Open Command Prompt as Administrator.\n"
            "- Run the following commands:\n"
            "  - DISM /Online /Cleanup-image /RestoreHealth - Repairs Windows image.\n"
            "  - sfc /scannow - Scans and repairs system files.\n"
            "- Restart your PC.",

            "Perform a System Restore:\n"
            "- Restoring to a previous state can resolve issues caused by recent changes.\n"
            "- Search 'Recovery' in the Start menu and open it.\n"
            "- Click 'Open System Restore' > Select 'Next'.\n"
            "- Choose a restore point > Click 'Finish' to restore.",

            "Reset the Device:\n"
            "- Resetting the PC resolves deeper, system-level issues.\n"
            "- Go to Settings > Update & Security.\n"
            "- Under 'Reset this PC', click 'Get Started'.\n"
            "- Choose 'Keep My Files' to reset the system while retaining personal data."
        ]
    }
}

gpu_issues = {
    "gpu driver timeout": {
        "error_name": "GPU Driver Timeout",
        "solutions": [
            "Disable Multi-Plane Overlay (MPO): You can use the Registry Editor to disable MPO.",
            "Change your power option: You can try changing your power option to the best performance mode.",
            "Restart your graphics driver: You can try restarting your graphics driver.",
            "Restart your PC: You can try restarting your PC and turning your monitor off and on again.",
            "Try a different video output: You can try using a different video output or a different display.",
            "Reseat your graphics card: You can try reseating your graphics card.",
            "Try a different graphics card slot: You can try using a different graphics card slot (if existing).",
            "Reinstall latest driver from GPU manufacturer website:\n"
            "- Uninstall old drivers using DDU (Display Driver Uninstaller).\n"
            "- Use the shortcut Windows key + Ctrl + Shift + B to reset your GPU driver.\n"
            "- Change PCIe power options."
        ]
    }
}

display_errors = {
    "hdmi not detected": {
        "error_name": "HDMI/Display Not Detected",
        "consideration": "This issue may be due to faulty cables, incorrect display settings, or GPU issues.",
        "solutions": [
            "Check if the HDMI / DisplayPort / VGA cable is properly connected.",
            "Try using a different cable or a different port to check if the cable is damaged.",
            "Ensure the HDMI / DP cable is plugged into the correct input/output port on both the PC and monitor.",
            "If using a dedicated GPU, ensure the HDMI / DP cable is connected to the GPU, not the motherboard.",
            "Ensure PCIe power cables are properly connected to the GPU.",
            "Reseat the graphics card (remove it from the PCIe slot and reconnect it).",
            "Try using a different monitor to check if the current monitor is faulty."
        ]
    }
}


def initialize_motherboard_data():
    """Creates motherboard objects and assigns beep code rules."""
    
    # IBM Beep Codes
    ibm = Motherboard("IBM")
    ibm.add_beep_code("1x short", "No errors detected during the self-test.")
    ibm.add_beep_code("2x short", "Error during the POST; more details displayed on screen.")
    ibm.add_beep_code("no beep (0)", "Power supply/system board/processor error; often related to power supply.")
    ibm.add_beep_code("continuous beep", "Power supply/system board/keyboard problem.")
    ibm.add_beep_code("repeated short beeps", "Power supply or system board problem.")
    ibm.add_beep_code("1x long, 1x short", "System board problem.")
    ibm.add_beep_code("1x long, 2x short", "Graphics card problem (Mono/CGA video error).")
    ibm.add_beep_code("1x long 3x short", "Graphics card problem (EGA video error).")
    ibm.add_beep_code("3x long", "Keyboard problem.")

    # Dell Beep Codes
    dell = Motherboard("Dell")
    dell.add_beep_code("1x short 1x short 2x short", "Keyboard controller test failure.")
    dell.add_beep_code("3x short 2x short 4x short", "Keyboard controller test failure.")
    dell.add_beep_code("3x short 3x short 1x short", "NVRAM power loss.")
    dell.add_beep_code("3x short 3x short 4x short", "Video memory test failure.")
    dell.add_beep_code("3x short 4x short 1x short", "Screen initialization failure.")
    dell.add_beep_code("4x short 2x short 2x short", "Shutdown failure.")
    dell.add_beep_code("4x short 4x short 4x short", "Cache test failure.")

    # Macintosh Beep Codes
    mac = Motherboard("Macintosh")
    mac.add_beep_code("3x short 5s pause 3x short", "RAM did not pass data integrity check.")
    mac.add_beep_code("1x long", "[Occurs while holding the power button] EFI ROM update in progress (for pre-2012 models).")
    mac.add_beep_code("3x long 2x short 3x long", "EFI ROM error or Mac is in EFI ROM recovery mode.")

    return {"IBM": ibm, "Dell": dell, "Macintosh": mac}


dll_crashes = {
    "User32.dll crash": {
        "error_name": "dll crashes",
        "solutions": [
            "Check to see if your program is using the User32.dll file.\n"
            "press the windows key + R and enter CMD to open the command prompt window and then enter the following command:\n"
            "tasklist /m User32.dll\n"
            "If the program does not show up in the tasklist, reinstall it.",
            
            "Ensure that your windows is up to date. To open the windows updater, use the following command in the command prompt window:\n"
            "wupdmgr",
            
            "Use the System File checker tool to repair the User32.dll file along with any other windows system files:\n"
            "Enter the command prompt and type: SFC /scannow\n"
            "restart your computer after the scan is finished and your files have been successfully validated.\n"
        ]
    }
}

directx_errors = {
    "directx compatibility issue": {
        "error_name": "DirectX Compatibility Errors",
        "solutions": [
            "Check If Your GPU Supports the Required DirectX Version:\n"
            "How:\n"
            "- Press Win + R, type dxdiag, and press Enter.\n"
            "- Look for DirectX Version under the System tab.\n"
            "- Compare it with the application/game requirements.\n"
            "- If your GPU does not support the required version, upgrading your GPU is the only option.",

            "Ensure DirectX Is Up-to-Date:\n"
            "While looking at the system requirements for a game, you might notice that there’s a specific DirectX requirement. In order to run the game, you need to make sure your DirectX is up-to-date with the game’s requirements.\n"
            "For example, Call of Duty requires you to have at least DirectX 11.\n"
            "1. Press the Windows + R keys on your keyboard. This is going to bring up the Run utility.\n"
            "2. Type in 'dxdiag' without the quotation marks and press the Enter key on your keyboard.\n"
            "Stay on the System tab, and look for the 'DirectX Version' line. Check if your current version is compatible with the game you’re trying to run. If not, you’ll need an update.\n"
            "If your version is outdated, update DirectX by:\n"
            "- Running Windows Update (Settings > Update & Security > Check for Updates).\n"
            "- Downloading the DirectX End-User Runtime from Microsoft’s official site. ( URL : https://www.microsoft.com/en-gb/download/details.aspx?id=35 )",

            "Install the DirectX Redistributable Package:\n"
            "How:\n"
            "- Download the DirectX End-User Runtimes (June 2010) from Microsoft. (URL : https://www.microsoft.com/en-gb/download/details.aspx?id=8109) \n"
            "- Run the installer and follow the on-screen instructions.\n"
            "- Restart your PC and try running the application again.",

            "Quit Third-Party Applications and Overlays:\n"
            "Some users have observed that not all video games support features like overlays. In some cases, your antivirus app may be the source of the issue. We’ve compiled a list of possible applications that may conflict with video games and cause the 'DirectX encountered an unrecoverable error' message.\n"
            "Try quitting the following applications, or disable the in-game overlay when possible:\n"
            "- MSI Afterburner\n"
            "- MSI DragonCentre\n"
            "- Riva Stats Server\n"
            "- Razer Cortex\n"
            "- GeForce Experience Overlay\n"
            "- Discord Overlay\n"
            "- Third-party antivirus applications\n"
            "After ensuring that none of these apps are running on your device, try to launch the problematic game again.",

            "Switch to a Legacy DirectX Version:\n"
            "How:\n"
            "- Open the game’s launcher settings (e.g., Steam, Epic Games, or manually in-game).\n"
            "- Look for an option to force DirectX 9, 10, or 11 instead of DirectX 12.\n"
            "- If available, use a launch option like:\n"
            "  -dx9\n"
            "  -dx11\n"
            "- Apply the changes and restart the game."
        ]
    }
}



low_fps_knowledge_base = {
    "monitor_connected_to_gpu": "Make sure your monitor is connected to your dedicated graphics card and not your CPU’s integrated graphics.",
    "gpu_drivers_updated": "Update your GPU drivers. Different workloads may require different driver versions.",
    "meets_system_requirements": "Check system requirements and upgrade components if needed.",
    "optimized_in_game_settings": "Reduce graphics settings to improve FPS.",
    "not_overheating": "Improve cooling, reapply thermal paste, or consider undervolting your CPU/GPU.",
    "correct_pcie_config": "Check BIOS settings to ensure GPU is in PCIE Gen 3 or Gen 4 mode.",
    "no_background_processes": "Close unnecessary background programs using Task Manager."
}


slow_pc_knowledge_base = {
    "pc_restarted": "Restart your PC to clear temporary files and refresh system processes.",
    "no_background_apps": "Close unnecessary background processes using Task Manager.",
    "startup_programs_disabled": "Disable startup programs in Task Manager.",
    "enough_disk_space": "Free up disk space and use Disk Cleanup.",
    "no_malware": "Run a full system malware scan.",
    "windows_and_drivers_updated": "Update Windows and system drivers.",
    "high_performance_mode": "Change power settings to High Performance in Control Panel.",
    "adjusted_visual_effects": "Disable unnecessary visual effects in 'Performance Options'.",
    "sfc_disk_check_done": "Run 'sfc /scannow' and 'chkdsk C: /f /r' in Command Prompt.",
    "sufficient_ram": "Consider upgrading your RAM for better multitasking.",
    "using_ssd": "Upgrade to an SSD for faster performance.",
    "windows_reset_done": "Reset Windows via Settings > Update & Security > Recovery."
}



malware_issues = {
    "virus": {
        "error_name": "virus",
        "consideration": "A computer virus is malicious code that infects files or programs, spreads across systems, and disrupts operations or damages data.",
        "solutions": [
            "Disconnect from the internet and run a Full System Scan:\n"
            "- Use trusted antivirus software like Windows Defender, Malwarebytes, or Norton.\n"
            "- Quarantine or delete infected files as recommended.",
            "Boot into Safe Mode:\n"
            "- Restart your PC and repeatedly press F8 (or Shift + Restart for Windows 10/11).\n"
            "- Run an antivirus scan in Safe Mode for better detection.",
            "Check Startup Entries:\n"
            "- Open Task Manager > Startup tab.\n"
            "- Disable any suspicious programs that automatically start.",
            "Update Software:\n"
            "- Keep your antivirus software and operating system up to date to patch vulnerabilities.",
            "Restore System Files:\n"
            "- Use the built-in System File Checker tool:\n"
            "  - Open Command Prompt as Administrator.\n"
            "  - Run the command: sfc /scannow.\n"
            "- Replace corrupted files with healthy versions.",
            "Reinstall Operating System (as a Last Resort):\n"
            "- If the infection is severe, back up your files, format your disk, and reinstall the operating system from a clean source."
        ]
    },

    "popups": {
        "error_name": "Excessive Pop-ups & Browser Redirects",
        "consideration": "This issue is often caused by browser hijackers, adware, or unwanted extensions.",
        "solutions": [
            "Reset Web Browsers to Default:\n"
            "- Chrome: Settings > Advanced > Reset Settings.\n"
            "- Firefox: Help > Troubleshoot Information > Refresh Firefox.\n"
            "- Edge: Settings > Reset Settings.",
            "Uninstall Suspicious Extensions:\n"
            "- Open your browser settings and navigate to 'Extensions'.\n"
            "- Remove any unknown or suspicious add-ons.",
            "Check Proxy Settings:\n"
            "- Open Run (Win + R) > Type 'inetcpl.cpl' > Connections tab > LAN settings.\n"
            "- Ensure 'Use a proxy server' is unchecked.",
            "Scan for Malware Using Malwarebytes:\n"
            "- Download and install Malwarebytes.\n"
            "- Perform a full system scan and remove detected threats."
        ]
    },

    "scareware": {
        "error_name": "scareware",
        "consideration": "Scareware tricks users into believing their PC is infected and urges them to install malicious software.",
        "solutions": [
            "Do NOT Click on the Pop-up:\n"
            "- Close the window using Task Manager (Ctrl + Shift + Esc > End Task).",
            "Boot into Safe Mode and Run a Full Antivirus Scan:\n"
            "- Restart your PC and repeatedly press F8 (or Shift + Restart for Windows 10/11).\n"
            "- Select Safe Mode with Networking.\n"
            "- Run a full scan with Windows Defender or a trusted antivirus.",
            "Uninstall Suspicious Software:\n"
            "- Open Control Panel > Programs & Features.\n"
            "- Look for unfamiliar programs installed recently and uninstall them.",
            "Check Hosts File for Redirects:\n"
            "- Open Notepad as Administrator > Open C:\\Windows\\System32\\drivers\\etc\\hosts.\n"
            "- Remove any suspicious entries redirecting websites (e.g., '127.0.0.1 facebook.com').",
            "Reset Network Settings:\n"
            "- Open Command Prompt as Administrator.\n"
            "- Run the following command: netsh winsock reset\n"
            "- Restart your PC."
        ]
    },

    "ransomware": {
        "error_name": "ransomware",
        "consideration": "Ransomware encrypts a victim's files, rendering them inaccessible until a ransom is paid.",
        "solutions": [
            "Isolate the Infected System:\n"
            "- Disconnect the device from the internet and other network connections immediately.\n"
            "- Disable shared drives to prevent the ransomware from spreading.",
            "Identify the Ransomware:\n"
            "- Use online tools like ID Ransomware (https://www.nomoreransom.org/).\n"
            "- Analyze the ransom note or file extensions to determine the ransomware strain.",
            "Use Decryption Tools (if available):\n"
            "- Visit No More Ransom (https://www.nomoreransom.org/) to find free decryption tools.\n"
            "- Download and use the tool for the identified ransomware strain.",
            "Boot into Safe Mode:\n"
            "- Restart your PC and repeatedly press F8 (or Shift + Restart for Windows 10/11).\n"
            "- Select Safe Mode with Networking.\n"
            "- Run antivirus software in Safe Mode.",
            "Run Antivirus/Malware Removal Tools:\n"
            "- Download and install trusted tools such as Malwarebytes or Kaspersky.\n"
            "- Perform a full system scan to detect and remove the ransomware.",
            "Restore from Backups:\n"
            "- If backups exist, format the infected system and restore files from a clean backup.\n"
            "- Ensure the backup is not connected to the infected system during recovery.",
            "Remove Ransomware Manually (Advanced):\n"
            "- Open Task Manager (Ctrl + Shift + Esc) and terminate suspicious processes.\n"
            "- Check startup programs via msconfig and disable malicious entries.\n"
            "- Open Registry Editor (regedit) and delete suspicious entries under:\n"
            "  HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run.",
            "Use Ransomware Recovery Features:\n"
            "- Check for shadow copies using the command: vssadmin list shadows.\n"
            "- Restore files using 'Previous Versions' in file properties.\n"
            "- On macOS, use Time Machine backups to recover files.",
            "Seek Professional Assistance:\n"
            "- Contact a cybersecurity professional or Incident Response team if unable to remove the ransomware.\n"
            "- Avoid negotiating with attackers directly.",
            "Rebuild and Reinstall:\n"
            "- As a last resort, wipe the device completely and reinstall the operating system.\n"
            "- Format all storage drives before reinstalling."
        ]
    },

    "adware": {
        "error_name": "adware",
        "consideration": "Adware displays intrusive ads or pop-ups and may redirect users to malicious websites, potentially compromising privacy.",
        "solutions": [
            "Uninstall Suspicious Programs:\n"
            "- Go to Control Panel > Programs & Features.\n"
            "- Locate and uninstall recently installed or unfamiliar programs.",
            "Remove Browser Extensions:\n"
            "- Check browser extensions or add-ons for anything suspicious.\n"
            "- Remove unfamiliar or unnecessary extensions.",
            "Reset Browser Settings:\n"
            "- Reset the browser to default settings to remove injected ads.\n"
            "- Clear cache and cookies.",
            "Use Anti-Adware Tools:\n"
            "- Download and run trusted anti-adware software like AdwCleaner or Malwarebytes.",
            "Block Pop-ups:\n"
            "- Enable the pop-up blocker in your browser settings.\n"
            "- Use browser extensions like uBlock Origin for additional protection."
        ]
    },
    "keylogger": {
    "error_name": "keylogger",
    "consideration": "Keyloggers monitor and record keystrokes to steal sensitive information, like passwords and credit card details.",
    "solutions": [
        "Run a Full Malware Scan:\n"
        "- Use a trusted antivirus or anti-keylogger tool.",
        "Check Task Manager for Suspicious Processes:\n"
        "- Identify and terminate unknown processes related to keyloggers.",
        "Uninstall Suspicious Software:\n"
        "- Remove recently installed or unfamiliar software.",
        "Use a Virtual Keyboard:\n"
        "- For sensitive tasks, use an on-screen virtual keyboard.",
        "Enable Multi factor authentication (MFA):\n"
        "- Secure online accounts with multi-factor authentication to mitigate stolen passwords."
    ]
    },
    "rootkits": {
    "error_name": "rootkits",
    "consideration": "Rootkits hide deep within the operating system, providing attackers persistent access while evading detection.",
    "solutions": [
    "Use Rootkit Removal Tools:\n"
    "- Run specialized tools like Kaspersky TDSSKiller or Malwarebytes Anti-Rootkit.",
    "Boot into Safe Mode:\n"
    "- Restart your PC and press F8 (or Shift + Restart for Windows 10/11).\n"
    "- Run an antivirus scan in Safe Mode.",
    "Update and Reinstall:\n"
    "- Update antivirus definitions and use them to clean the system.\n"
    "- As a last resort, format the system and reinstall the operating system."
    ]
    
    },

    "trojan": {
    "error_name": "trojan",
    "consideration": "Trojan horses disguise themselves as legitimate software while secretly performing malicious activities, like opening backdoors.",
    "solutions": [
        "Identify and Remove Suspicious Files:\n"
        "- Use Task Manager (Ctrl + Shift + Esc) to identify suspicious processes.\n"
        "- Locate and delete associated files.",
        "Run a Malware Scan:\n"
        "- Use trusted antivirus tools to detect and remove Trojans.",
        "Check and Remove Startup Entries:\n"
        "- Open Task Manager > Startup tab and disable unknown programs.",
        "Reinstall Compromised Applications:\n"
        "- If a Trojan masquerades as a legitimate app, uninstall and download the app from an official source.",
        "Harden Security Settings:\n"
        "- Enable a firewall and real-time protection in your antivirus software."
    ]
      }
    }
  









# -----------------------------
#  BACKWARD CHAINING FUNCTION -NETWORK ISSUES
# -----------------------------
def backward_chaining_network():
    
    print("\nLet's resolve your network issues...")
    
    problem = input("\nWhat is the network issue you're facing? \nOptions: "
                    "\n1) Weak Wi-Fi signal"
                    "\n2) High latency"
                    "\n3) Unable to access a website"
                    "\n4) Slow download speeds"
                    "\n5) Inconsistent connection"
                    "\n6) Missing Wi-Fi option \nEnter the number of your issue:").strip()
    
    if problem == "1":  # Weak Wi-Fi signal
        if input("\nAre you far from the router? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Move closer to the router or use an Ethernet cable.")
        elif input("\nAre there walls or obstacles blocking the signal? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Remove obstacles or place the router in a central, open area.")
        elif input("\nIs the router outdated or damaged? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Consider upgrading your router.")
        else:
            print("\n Solution: Reset your router and check for firmware updates.")

    elif problem == "2":  # High latency
        if input("\nAre you connected to a server in a far region? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to a server region closer to you.")
        elif input("\nIs your internet connection speed low? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Contact your ISP to upgrade your plan or troubleshoot slow speeds.")
        elif input("\nAre background applications consuming bandwidth? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Close unnecessary applications and downloads.")
        else:
            print("\n Solution: Restart your router and prioritize devices on your network.")

    elif problem == "3":  # Unable to access a website
        if input("\nIs the website blocked by a firewall? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Configure your firewall to whitelist the website.")
        elif input("\nIs the website blocked in your region? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Use a VPN to access the website.")
        elif input("\nIs your DNS server misconfigured? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to a public DNS (e.g., Google DNS: 8.8.8.8).")
        else:
            print("\n Solution: Clear your browser cache or try accessing the website from a different device.")

    elif problem == "4":  # Slow download speeds
        if input("\nAre you using a 2.4GHz Wi-Fi band? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Switch to the 5GHz band or use an Ethernet cable.")
        elif input("\nAre there too many devices on your network? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Disconnect unused devices to free up bandwidth.")
        elif input("\nIs your internet plan sufficient for your needs? (yes/no): ").strip().lower() == "no":
            print("\n Solution: Upgrade to a higher-speed internet plan.")
        else:
            print("\n Solution: Restart your router and avoid peak usage times.")

    elif problem == "5":  # Inconsistent connection
        if input("\nHave you tried flushing your DNS cache? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Open the command prompt and enter 'ipconfig /flushdns'.")
        elif input("\nIs your router overheating or old? (yes/no): ").strip().lower() == "yes":
            print("\n Solution: Replace the router or ensure proper ventilation.")
        elif input("\nIs your ISP experiencing outages? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Contact your ISP for updates on the issue.")
        else:
            print("\nSolution: Test your connection with another device or network.")

    elif problem == "6":  # Missing Wi-Fi option
        if input("\nIs your network driver up to date? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Open Device Manager, reinstall your network driver, and reboot.")
        elif input("\nIs your Wi-Fi card properly installed? (yes/no): ").strip().lower() == "no":
            print("\nSolution: Ensure your Wi-Fi card is correctly connected to the motherboard.")
        elif input("\nIs airplane mode enabled? (yes/no): ").strip().lower() == "yes":
            print("\nSolution: Disable airplane mode in your system settings.")
        else:
            print("\nSolution: Check your BIOS settings to ensure the Wi-Fi card is enabled.")

    else:
        print("\nNo solution found. Consider contacting your Internet Service Provider (ISP).")









# -----------------------------
# FRAME-BASED REPRESENTATION 
# -----------------------------


class Motherboard:
    """Base class representing a motherboard brand and its beep codes."""
    def __init__(self, brand):
        self.brand = brand
        self.beep_codes = {}  # Dictionary to store beep codes and their meanings

    def add_beep_code(self, code, meaning):
        """Adds beep code error information to the motherboard class (stored in lowercase for case-insensitivity)."""
        self.beep_codes[code.lower()] = meaning  # Store beep codes in lowercase for case-insensitive matching

    def diagnose_beep_code(self, code):
        """Checks the beep code against the stored rules and returns the diagnosis (case insensitive)."""
        code_lower = code.lower()  # Convert user input to lowercase
        if code_lower in self.beep_codes:
            return f"Detected Issue for {self.brand}: {self.beep_codes[code_lower]}"
        return "Beep code not recognized. Check the manufacturer’s manual."







# -----------------------------
# FORWARD CHAINING FUNCTION (Rule-Based System)
# -----------------------------
def forward_chaining(category, key):
    """Matches known error conditions with solutions using forward chaining and interactive troubleshooting."""
    
    # Define category rule sets
    rule_sets = {
        "BSOD": bsod_errors,
        "GPU": gpu_issues,
        "DirectX": directx_errors,
        "DLL Errors": dll_crashes,       
        "Malware": malware_issues,
        "Display": display_errors
    }
    
    # Check if the error exists in the selected category
    if category in rule_sets and key in rule_sets[category]:
        error_data = rule_sets[category][key]

        #  Display the detected error
        print(f"\nDetected {category} Error: {key} - {error_data['error_name']}")

        #  Display consideration message if available
        if "consideration" in error_data:
            print(f"\nConsideration: {error_data['consideration']}")

        #  Loop through solutions step-by-step
        solutions = error_data["solutions"]
        for i, solution in enumerate(solutions, start=1):
            print(f"\nSuggested Solution {i}: {solution}")
            
            #  Ask the user if the solution worked
            response = input("\nDid this solution work? (yes/no): ").strip().lower()

            # Ensure valid input
            while response not in ["yes", "no"]:
                response = input("Invalid input! Please enter 'yes' or 'no': ").strip().lower()

            #  If the solution worked, stop troubleshooting
            if response == "yes":
                print("\n Thank you for using our system! Your issue has been resolved.")
                return  

        #  If no solution worked, suggest contacting support
        print("\nNo solution worked, consider seeking further assistance.")
    else:
        print("\nError not found. Please check online resources.")








# -----------------------------
# BACKWARD CHAINING FUNCTION  
# -----------------------------
def backward_chaining_beep_code():
    """Asks the user to input beep code details and applies backward chaining to diagnose the issue."""
    motherboards = initialize_motherboard_data()
    
    print("\nMotherboard Beep Code Troubleshooting")
    print("Supported Brands: IBM, Dell, Macintosh")
    
    brand = input("\nEnter your motherboard brand: ").strip().capitalize()  # Fix: Normalize input case

    # Fix: Allow case-insensitive matching for brands
    brand_mapping = {key.lower(): key for key in motherboards.keys()}  # Create lowercase mapping
    brand_lower = brand.lower()

    if brand_lower not in brand_mapping:
        print("Unsupported motherboard brand. Please check the manufacturer’s manual.")
        return

    selected_brand = brand_mapping[brand_lower]  # Get correct key format for dictionary lookup

    beep_code = input("Enter the beep code pattern (e.g., '1x short', '3x long', 'continuous beep'): ").strip().lower()
    diagnosis = motherboards[selected_brand].diagnose_beep_code(beep_code)

    print(f"\n{diagnosis}")


def backward_chaining(problem, knowledge_base):
    """Inference Engine: Applies Backward Chaining to diagnose the issue."""
    print(f"\n Diagnosing {problem}...")

    for solution, condition in knowledge_base.items():
        response = input(f"\nDid you? {condition.replace('_', ' ').capitalize()}? (yes/no): ").strip().lower()

        while response not in ["yes", "no"]:
            response = input("Invalid input! Please enter 'yes' or 'no': ").strip().lower()

        if response == "no":
            print(f"\n Solution: {condition}")
            return  # Stop once a solution is found

    print("\n No clear cause found. Consider hardware upgrades or consulting a specialist.")

    

# -----------------------------
# GENERAL TROUBLESHOOTING WIZARD 
# -----------------------------

def general_troubleshooting_wizard():
    """Allows the user to select between Low FPS Troubleshooting and Slow PC Performance Troubleshooting."""
    print("\n General Troubleshooting Wizard")
    print("1. Troubleshoot Low FPS in Games")
    print("2. Troubleshoot Lag / Slow PC Performance")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        backward_chaining("Low FPS in Games", low_fps_knowledge_base)
    elif choice == "2":
        backward_chaining("Lag / Slow PC Performance", slow_pc_knowledge_base)
    else:
        print("Invalid selection. Returning to the main menu.")

















          

# -----------------------------
#  MAIN FUNCTION MENU (User Interaction)
# -----------------------------
def main(): 
    print("\nWelcome to the PC Tech Support Expert System by Bruno Cimo and Hishaam Mehmood!")
    print("\nSelect an issue:")
    print("1. BSOD Error")
    print("2. GPU Issues")
    print("3. Display Errors")
    print("4. Motherboard Beep Codes")
    print("5. Crashes & DLL Errors")
    print("6. DirectX Compatibility Issues")
    print("7. Network Issues")
    print("8. General Troubleshooting Wizard")
    print("9. Malware & Virus Issues")

    choice = input("\nEnter your choice (1-9): ").strip()

    if choice == "1":
        code = input("Enter the BSOD error code: ").strip()
        print(forward_chaining("BSOD", code))
    elif choice == "2":
        print("\n GPU Troubleshooting: GPU Driver Timeout")
        forward_chaining("GPU", "gpu driver timeout")
    elif choice == "3":
        print("\nDisplay Troubleshooting:")
        (forward_chaining("Display", "hdmi not detected"))
    elif choice == "4":
        backward_chaining_beep_code()
    elif choice == "5":
        print("\nDLL or Game Crash Troubleshooting:")
        print(forward_chaining("DLL Errors", "User32.dll crash"))
        
    elif choice == "6":
        print("\nDirectX Compatibility Troubleshooting:")

        # Automatically display DirectX troubleshooting solutions
        forward_chaining("DirectX", "directx compatibility issue")

    elif choice == "7":
        print("\nNetwork Troubleshooting:")
        backward_chaining_network()
        
    if choice == "8":
        (general_troubleshooting_wizard())
    elif choice == "9":
        print("\nMalware & Virus Troubleshooting:")
        malware_type = input("Please enter the malware type: ").strip()
        print(forward_chaining("Malware", malware_type))
    else:
        print("Invalid selection. Returning to main menu.")

# Runs the expert system
if __name__ == "__main__":
    main()
